from processors import Data, Text, Image


class Ranker:
    def __init__(self,training_path, testing_path, n_classes):
        self.data = Data(training_path, testing_path, n_classes)

        self.text = Text(self.data)
        self.text.do_test_clasifiers()

        #self.image = Image(self.data)
        #self.image.do_test_clasifiers()



