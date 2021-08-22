from app.models import Review, User
from app import db


def setUp(self):
    self.user_felix = User(
        username="felix", password="kodhanjo", email="felix339575@gmail.com"
    )
    self.new_review = Review(
        pitch_id=12345,
        pitch_title="Review for pitches",
        image_path="https://e7.pngegg.com/pngimages/469/75/png-clipart-http-404-web-page-error-product-design-hypertext-transfer-protocol-error-electronics-text-thumbnail.png",
        pitch_review="This pitch is the best thing since sliced bread",
        user=self.user_felix,
    )


def tearDown(self):
    Review.query.delete()
    User.query.delete()


def test_check_instance_variables(self):
    self.assertEquals(self.new_review.pitch_id, 12345)
    self.assertEquals(
    self.new_review.pitch_review, "This pitch is the best thing since sliced bread"
    )
    self.assertEquals(self.new_review.user, self.user_felix)


def test_save_review(self):
    self.new_review.save_review()
    self.assertTrue(len(Review.query.all()) > 0)


def test_get_review_by_id(self):
    self.new_review.save_review()
    got_reviews = Review.get_reviews(12345)
    self.assertTrue(len(got_reviews) == 1)
