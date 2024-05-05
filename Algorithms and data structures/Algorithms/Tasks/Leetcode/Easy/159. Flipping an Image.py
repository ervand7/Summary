from typing import List


# my solution (not well)
def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
    for i in image:
        len_i = len(i)
        for j in range((len_i + 1) // 2):
            temp = i.copy()
            i[j] = 0 if temp[len_i - j - 1] == 1 else 1
            i[len_i - j - 1] = 0 if temp[j] == 1 else 1

    return image


# ChatGPT solution (good and more effective)
def flip_and_invert_image(image):
    n = len(image)
    for row in image:
        # Reverse the row and invert each element in one pass
        for i in range((n + 1) // 2):  # (n+1)//2 ensures that the middle element in an odd-length row is also processed
            # Flip and invert elements at the same time
            # If the elements are the same, flipping them and then inverting will result in both being inverted
            # If the elements are different, flipping and inverting will swap their values, since 1 becomes 0 and 0 becomes 1
            row[i], row[n - 1 - i] = 1 - row[n - 1 - i], 1 - row[i]

    return image
