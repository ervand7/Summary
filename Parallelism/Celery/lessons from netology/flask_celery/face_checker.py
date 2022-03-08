import os

import dlib  # заранее обученная нейросеть
from skimage.io import imread
from scipy.spatial import distance


class FaceChecker:
    instance = None

    def __init__(self, shape_predictor, face_model):
        self.shape_predictor = shape_predictor
        self.face_model = face_model
        self.face_detector = dlib.get_frontal_face_detector()

    @classmethod
    def with_files(cls,
                   shape_predictor_path=os.path.join('models', 'shape_predictor_68_face_landmarks.dat'),
                   face_model_path=os.path.join('models', 'dlib_face_recognition_resnet_model_v1.dat')):
        if not cls.instance:
            shape_predictor = dlib.shape_predictor(shape_predictor_path)
            face_model = dlib.face_recognition_model_v1(face_model_path)
            cls.instance = cls(shape_predictor, face_model)
        return cls.instance

    def load_image(self, path: str, visual=False):
        img = imread(path)
        rectangles = self.face_detector(img, 0)
        shape = self.shape_predictor(img, rectangles[0])
        if visual:
            window = dlib.image_window()
            window.clear_overlay()
            window.set_image(img)

            window.add_overlay(rectangles)
            window.add_overlay(shape)
            window.wait_until_closed()

        descriptor = self.face_model.compute_face_descriptor(img, shape)
        return descriptor

    def match(self, img_path_1: str, img_path_2: str, visual=False):
        """
        Определяет на лицах ключевые вектора и вычисляет евклидовую разницу
        векторов лица одного человека от векторов лица другого человека.
        Если разница меньше, чем 0.6, мы считаем, что это один и тот же человек.
        Уменьшая этот коэффицент6 мы ужесточаем проверку.
        """
        return distance.euclidean(self.load_image(img_path_1, visual), self.load_image(img_path_2, visual), ) < 0.6
