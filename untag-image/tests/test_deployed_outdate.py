import test_keep_deployed_version_template as template

untag_list = ['1.0.38', '1.0.37', '1.0.36', '1.0.35', '1.0.34']
expected_list = ['1.0.34']


def test_deployed_outdated():
    result = template.keep_deployed_version(tag_list=template.tag_list, untag_list=untag_list)
    assert result == expected_list
