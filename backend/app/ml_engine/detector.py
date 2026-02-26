from retina_face import RetinaFace

def detect_face(image_path):
    return RetinaFace.detect_faces(image_path)
