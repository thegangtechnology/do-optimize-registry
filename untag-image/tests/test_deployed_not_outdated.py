import test_keep_deployed_version_template as template

untag_list = []
expected_list = []


def test_deployed_outdated():
    result = template.keep_deployed_version(tag_list=template.tag_list, untag_list=untag_list)
    assert result == expected_list
