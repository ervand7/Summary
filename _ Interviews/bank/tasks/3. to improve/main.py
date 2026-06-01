@app.post("/transfers")
def create_transfer(req: TransferRequest, db: Session):
    # the sender is taken from the request payload
    sender_id = req.user_id

    sender = db.query(Account).filter(Account.user_id == sender_id).first()

    # check funds, then move the money
    if sender.balance >= req.amount:
        sender.balance = sender.balance - req.amount
        receiver = db.query(Account).filter(Account.id == req.to_account_id).first()
        receiver.balance = receiver.balance + req.amount
        db.commit()
        send_email(sender.email, "You sent " + str(req.amount))
        return {"status": "ok"}
    return {"status": "insufficient_funds"}

"""
1. **Security issue**
   * ❌ `sender_id = req.user_id` from payload can be spoofed
   * ✅ take user id from authenticated context/JWT/session

2. **No transaction handling**
   * ❌ partial DB updates possible
   * ✅ wrap in transaction (`with db.begin()`), rollback on error

3. **Race condition / double spending**
   * Two requests can read the same balance simultaneously
   * ✅ use row locking (`SELECT FOR UPDATE`) or atomic DB update

4. **No validation**

   * Check:

     * amount > 0
     * receiver exists
     * sender exists
     * sender != receiver

5. **No error handling**
   * `.first()` can return `None`
   * `sender.balance` → crash

6. **External call inside business flow**
   * ❌ `send_email()` after commit but synchronously
   * ✅ publish event/message queue (Kafka/Celery/RabbitMQ)

7. **Mixing layers**
   * Controller contains business logic
   * ✅ move transfer logic to service layer

8. **Money stored incorrectly**
   * ❌ avoid float for money
   * ✅ use Decimal / integer cents

9. **No idempotency**
   * Retried HTTP request may create duplicate transfers
   * ✅ use idempotency key / transaction id

10. **No audit/history**
* Balance changes without transaction records
* ✅ create immutable `transactions` table

11. **Bad HTTP responses**
* ❌ `{"status":"insufficient_funds"}`
* ✅ proper HTTP codes (400, 404, etc.)

12. **No observability**
* Add logs, metrics, tracing
"""


from decimal import Decimal
from fastapi import HTTPException

@app.post("/transfers")
def create_transfer(
    req: TransferRequest,
    db: Session,
    current_user: User,  # from JWT/auth middleware
):
    if req.amount <= 0:
        raise HTTPException(400, "amount must be positive")

    if current_user.account_id == req.to_account_id:
        raise HTTPException(400, "cannot transfer to yourself")

    with db.begin():
        sender = (
            db.query(Account)
            .filter(Account.user_id == current_user.id)
            .with_for_update()
            .first()
        )

        receiver = (
            db.query(Account)
            .filter(Account.id == req.to_account_id)
            .with_for_update()
            .first()
        )

        if sender is None:
            raise HTTPException(404, "sender not found")

        if receiver is None:
            raise HTTPException(404, "receiver not found")

        if sender.balance < req.amount:
            raise HTTPException(400, "insufficient funds")

        sender.balance -= req.amount
        receiver.balance += req.amount

        db.add(
            Transaction(
                from_account_id=sender.id,
                to_account_id=receiver.id,
                amount=req.amount,
            )
        )

    send_email(sender.email, f"You sent {req.amount}")

    return {"status": "ok"}