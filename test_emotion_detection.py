import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotions(self):
        self.assertEqual(emotion_detector("I am glad")["dominant_emotion"], "joy")
        self.assertEqual(emotion_detector("I am mad")["dominant_emotion"], "anger")
        self.assertEqual(emotion_detector("I am disgusted")["dominant_emotion"], "disgust")
        self.assertEqual(emotion_detector("I am sad")["dominant_emotion"], "sadness")
        self.assertEqual(emotion_detector("I am afraid")["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()