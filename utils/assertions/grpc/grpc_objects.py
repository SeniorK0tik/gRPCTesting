from typing import Pattern

from utils.assertions.base.expect import expect



def assert_grpc_example(expected_text: str, actual_text: str, regex: Pattern[str]):
    expect(expected_text) \
        .set_description('GRPC object') \
        .is_typeof(actual_text, str) \
        .is_match(actual_text, regex)