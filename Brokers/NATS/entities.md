### 📡 **NATS (Cloud Native Messaging System)**

Official website: [https://nats.io](https://nats.io)
Lightweight, high-performance messaging system designed for microservices, IoT, and real-time systems.

---

### ● **Core Concepts (NATS Core)**

#### 🔑 **Subject**

* Like a **topic** in Kafka.
* String-based identifier (e.g., `orders.created`, `user.signup`).
* Supports **wildcards**:

  * `>` — matches everything after (e.g., `orders.>`)
  * `*` — matches one token (e.g., `orders.*`)

#### 📨 **Publisher / Subscriber (Pub/Sub)**

* **Publisher** sends messages to a subject.
* **Subscriber** listens to messages on a subject.
* Many-to-many model.
* **Fire-and-forget**, no built-in durability or replay in NATS Core.

#### 👥 **Queue Groups**

* Multiple subscribers can join the same queue group.
* Within one group, **only one subscriber receives each message** — load balancing.
* Like Kafka’s **consumer group** but **simpler**.

---

### ● **JetStream (Optional Add-on for Durability, Replay, Persistence)**

JetStream adds Kafka-like features to NATS.

#### 💾 **Persistence**

* Messages are **stored** on disk or memory.
* Configurable retention policies:

  * **Limits** (size/count)
  * **Interest-based** (only kept if someone is listening)
  * **Work Queue** (deleted after acknowledgment)

#### 🧾 **Streams**

* Like **topics**, but persistent.
* Messages are retained in a stream.
* One stream = one subject (or wildcard match).

#### 🧑‍💻 **Consumers**

* Pull-based (you request messages) or push-based (JetStream pushes to you).
* You can **replay** messages, set start position by:

  * Time
  * Sequence number
  * Last N messages

#### 🔁 **Message Acknowledgment & Redelivery**

* Must **acknowledge** (`ack`) messages to mark them as processed.
* Unacked messages are redelivered after a timeout.

#### 📦 **Durable Consumer**

* Keeps its state (like Kafka consumer offset).
* You can resume where you left off.

---

### ● **Delivery Guarantees**

* **At-most-once** in NATS Core (no persistence).
* **At-least-once** in JetStream (with ack).
* **Exactly-once** — not native, needs app-level deduplication.

---

### ● **NATS Server (nats-server)**

* Lightweight binary, <10MB.
* No external dependencies (like ZooKeeper in Kafka).
* Supports **clustering** (for HA and load).

---

### ● **Monitoring & Observability**

* Built-in **metrics endpoint** for Prometheus.
* Admin tools: `nats` CLI, JetStream CLI (`nats stream`, `nats consumer`).

---

### ● **Performance**

* Millions of messages per second per server.
* Very low latency (<1ms).
* Designed for real-time systems and low resource usage.

---

### ● **Security**

* TLS encryption
* Token-based or NKey auth
* Account isolation and user permissions

---

### ● **Comparison with Kafka**

| Feature             | Kafka                            | NATS Core               | NATS JetStream        |
| ------------------- | -------------------------------- | ----------------------- | --------------------- |
| Message persistence | ✅ Always                         | ❌ (fire-and-forget)     | ✅ (optional)          |
| Replay messages     | ✅                                | ❌                       | ✅                     |
| Message ordering    | ✅ per partition                  | ❌ no ordering guarantee | ✅ per stream          |
| Consumer groups     | ✅                                | ✅ (via Queue Groups)    | ✅ (durable consumers) |
| Scaling             | High, but heavier                | Extremely lightweight   | Still lightweight     |
| Dependencies        | Needs ZooKeeper (for Kafka <2.8) | ❌                       | ❌                     |
