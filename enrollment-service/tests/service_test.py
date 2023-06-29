from unittest.mock import patch, call

import pytest

from app.enrollment_service import EnrollmentService
from app.repositories.enrollment_repository import EnrollmentRepository
from app.models.enrollment import Enrollment


class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data


def test_enroll_student_in_class_success():
    student_id = 1
    student_response_data = {'id': student_id, 'name': 'John Doe'}
    student_response = MockResponse(200, json_data=student_response_data)

    subject_num = 123
    class_num = 456
    subject_response_data = {
        'subject_num': subject_num, 'class_num': class_num}
    subject_response = MockResponse(200, json_data=subject_response_data)

    with patch('requests.get') as mock_get:
        mock_get.side_effect = [student_response, subject_response]

        with patch.object(EnrollmentRepository, 'create_enrollment') as mock_repository:
            enrollment_fake = Enrollment.from_dict({
                'subject_num': subject_num,
                'class_num': class_num,
                'student_id': student_id
            })

            mock_repository.return_value = enrollment_fake

            enrollment = EnrollmentService.enroll_student_in_class(
                student_id, subject_num, class_num)

    assert enrollment == enrollment_fake

    mock_get.assert_has_calls([
        call(f'http://student-app:80/{student_id}'),
        call(f'http://subject-app:80/{subject_num}&{class_num}')
    ])


def test_enroll_student_in_class_retrieve_student_failed():
    student_id = 1
    student_response = MockResponse(500)

    subject_num = 123
    class_num = 456
    subject_response_data = {
        'subject_num': subject_num, 'class_num': class_num}
    subject_response = MockResponse(200, json_data=subject_response_data)

    with patch('app.enrollment_service.jsonify', return_value={'error': 'Failed to retrieve student information.'}):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = [student_response, subject_response]

            result = EnrollmentService.enroll_student_in_class(
                student_id, subject_num, class_num)

    assert result == (
        {'error': 'Failed to retrieve student information.'}, 500)


def test_enroll_student_in_class_retrieve_subject_failed():
    student_id = 1
    student_response_data = {'id': student_id, 'name': 'John Doe'}
    student_response = MockResponse(200, json_data=student_response_data)

    subject_num = 123
    class_num = 456
    subject_response = MockResponse(500)

    with patch('app.enrollment_service.jsonify', return_value={'error': 'Failed to retrieve student information.'}):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = [student_response, subject_response]

            result = EnrollmentService.enroll_student_in_class(
                student_id, subject_num, class_num)

    assert result == (
        {'error': 'Failed to retrieve student information.'}, 500)
