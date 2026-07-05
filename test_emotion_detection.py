"""Unit tests for the emotion_detector function."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases verifying the dominant emotion for sample statements."""

    def test_emotion_detector(self):
        """Check that each sample statement returns the expected dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

        result = emotion_detector("I am so terrified about this")
        self.assertEqual(result['dominant_emotion'], 'fear')

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == '__main__':
    unittest.main()
