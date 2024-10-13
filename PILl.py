import os
import random
import cv2
import numpy as np
import time
def augment_image(image):
    # Применение различных фильтров и эффектов для создания искусственного вида
    if random.random() > 0.5:
        image = cv2.flip(image, 1)
        time.sleep(1)

    if random.random() > 0.5:
        brightness = random.randint(-50, 50)
        image = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
        time.sleep(1)

    if random.random() > 0.5:
        alpha = random.uniform(1.2, 1.5)
        image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
        time.sleep(1)

    if random.random() > 0.5:
        image = cv2.GaussianBlur(image, (15, 15), 0)
        time.sleep(1)

    if random.random() > 0.5:
        image = cv2.medianBlur(image, 5)
        time.sleep(1)

    noise = np.random.randint(0, 50, image.shape, dtype='uint8')
    image = cv2.add(image, noise)

    if random.random() > 0.5:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv[..., 0] = (hsv[..., 0] + random.randint(0, 180)) % 180
        image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        time.sleep(1)

    return image


def generate_augmented_images(input_folder, output_folder, num_images=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    all_images = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]

    if len(all_images) == 0:
        print(input_folder)
        print("Нет доступных изображений в выбранной папке.")
        return

    augmented_count = 0
    while augmented_count < num_images:
        filename = random.choice(all_images)
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        augmented_image = augment_image(image)
        output_path = os.path.join(output_folder, f'generated_{augmented_count}.jpg')

        cv2.imwrite(output_path, augmented_image)
        augmented_count += 1


def main(options={}):
    # Получаем список доступных датасетов

    f = []
    for i in options.keys():
        print(i)
        for j in options[i]["values"]:
            f.append(["palmar/" + i + "/" + j, int(options[i]["quantity"])])
    print(f)
    datasets = f


    # print("Выберите датасет:")
    # for i, dataset in enumerate(datasets):
    #     print(f"{i + 1}: {dataset}")

    # choice = int(input("Введите номер датасета: ")) - 1

    # if choice < 0 or choice >= len(datasets):
    #     print("Неверный выбор. Завершение программы.")
    #     return

    # input_folder = datasets[choice]
    for i in f:
        input_folder = i[0]
        num_images = i[1]

        output_folder = 'Output'
        # num_images = 8  # Количество изображений для генерации

        generate_augmented_images(input_folder, output_folder, num_images)
if __name__ == "__main__":
    main()
