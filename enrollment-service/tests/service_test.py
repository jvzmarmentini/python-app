import pytest
from unittest.mock import patch
from app.repositories.enrollment_service import EnrollmentService


class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data


class MockEnrollment:
    def __init__(self, subject_num, class_num, student_id):
        self.subject_num = subject_num
        self.class_num = class_num
        self.student_id = student_id


@pytest.fixture(scope='module')
def mocked_authenticate():
    with patch('app.login_required_decorator.authenticate') as mock:
        mock.return_value = True
        yield mock


def test_enroll_student_in_class_success():
    service = EnrollmentService()
    student_id = 1
    subject_num = 'ENG101'
    class_num = 'A101'

    with patch('requests.get') as mock_get:
        with patch.object(service, 'enroll_student_in_class') as mock_enroll:
            mock_get.side_effect = [
                MockResponse(200, {'student_id': student_id}),
                MockResponse(
                    200, {'subject_num': subject_num, 'class_num': class_num})
            ]

            service.enroll_student_in_class(student_id, subject_num, class_num)

            mock_enroll.assert_called_once_with(
                student_id, subject_num, class_num)


# def test_enroll_student_in_class_failed_to_retrieve_student_info():
#     service = EnrollmentService()
#     student_id = 1
#     subject_num = 'ENG101'
#     class_num = 'A101'

#     with patch('requests.get') as mock_get:
#         mock_get.return_value = MockResponse(500)

#         response = service.enroll_student_in_class(
#             student_id, subject_num, class_num)

#         # Assert that an error message and status code 500 were returned
#         assert response.status_code == 500
#         assert response.json_data == {
#             'error': 'Failed to retrieve student information.'}


# def test_enroll_student_in_class_failed_to_retrieve_subject_info():
#     service = EnrollmentService()
#     student_id = 1
#     subject_num = 'ENG101'
#     class_num = 'A101'

#     with patch('requests.get') as mock_get:
#         mock_get.side_effect = [
#             MockResponse(200, {'student_id': student_id}),
#             MockResponse(500)
#         ]

#         response = service.enroll_student_in_class(
#             student_id, subject_num, class_num)

#         # Assert that an error message and status code 500 were returned
#         assert response.status_code == 500
#         assert response.json_data == {
#             'error': 'Failed to retrieve subject information.'}


# def test_list_enrollments():
#     service = EnrollmentService()

#     # Mock the enrollments
#     enrollment1 = MockEnrollment('ENG101', 'A101', 1)
#     enrollment2 = MockEnrollment('MATH202', 'B202', 2)
#     enrollment3 = MockEnrollment('SCI303', 'C303', 1)
#     service.enrollments = [enrollment1, enrollment2, enrollment3]

#     enrollments = service.list_enrollments()

#     # Assert that the enrollments were retrieved correctly
#     assert len(enrollments) == 3
#     assert enrollments[0].subject_num == enrollment1.subject_num
#     assert enrollments[0].class_num == enrollment1.class_num
#     assert enrollments[0].student_ids == [enrollment1.student_id]
