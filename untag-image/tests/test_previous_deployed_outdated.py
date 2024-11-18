import test_untag_list_template

tag_list = ['develop', '0.3.0-14', '0.3.0-13', '0.3.0-12', '0.3.0-11', '0.3.0-10', '0.3.0-9', '0.3.0-8', '0.3.0-7',
            '0.3.0-6', '0.3.0-5', '0.3.0-4', '0.3.0-2', '0.3.0-1', '0.3.0', '0.2.19-12', '0.2.19-11', '0.2.19-10',
            '0.2.19-9', '0.2.19-8', '0.2.19-7', '0.2.19-6', '0.2.19-5', '0.2.19-4', '0.2.19-3', '0.2.19-2', '0.2.19-1',
            '0.2.19', '0.2.18-10', '0.2.18-9', '0.2.18-8', '0.2.18-7', '0.2.18-6', '0.2.18-5', '0.2.18-2', '0.2.18-1',
            '0.2.18', '0.2.17-9', '0.2.17-8', '0.2.17-7', '0.2.17-6', '0.2.17-5', '0.2.17-4', '0.2.17-3', '0.2.17-2',
            '0.2.17-1', '0.2.17', '0.2.16-6', '0.2.16-5', '0.2.16-4', '0.2.16-2', '0.2.16-1', '0.2.16', '0.2.15-12',
            '0.2.15-11', '0.2.15-10', '0.2.15-9', '0.2.15-8', '0.2.15-7', '0.2.15-6', '0.2.15-5', '0.2.15-4',
            '0.2.15-3', '0.2.15-2', '0.2.15-1', '0.2.15', '0.2.14-6', '0.2.14-5', '0.2.14-4', '0.2.14-3', '0.2.14-1',
            '0.2.14', '0.2.13-11', '0.2.13-10', '0.2.13-9', '0.2.13-8', '0.2.13-7', '0.2.13-6', '0.2.13-5', '0.2.13-4',
            '0.2.13-3', '0.2.13-2', '0.2.13-1', '0.2.13', '0.2.12-13', '0.2.12-12', '0.2.12-9', '0.2.12-8', '0.2.12-7',
            '0.2.12-6', '0.2.12-5', '0.2.12-4', '0.2.12-3', '0.2.12-2', '0.2.12-1', '0.2.12', '0.2.11-11', '0.2.11-10',
            '0.2.11-9', '0.2.11-7', '0.2.11-6', '0.2.11-5', '0.2.11-4', '0.2.11-3', '0.2.11-2', '0.2.11-1', '0.2.11',
            '0.2.10-23', '0.2.10-22', '0.2.10-21', '0.2.10-20', '0.2.10-19', '0.2.10-18', '0.2.10-17', '0.2.10-16',
            '0.2.10-15', '0.2.10-14', '0.2.10-13', '0.2.10-12', '0.2.10-9', '0.2.10-8', '0.2.10-7', '0.2.10-6',
            '0.2.10-5', '0.2.10-4', '0.2.10-3', '0.2.10-1', '0.2.10', '0.2.9-8', '0.2.9-7', '0.2.9-6', '0.2.9-5',
            '0.2.9-4', '0.2.9-3', '0.2.9-2', '0.2.9-1', '0.2.9', '0.2.8-14', '0.2.8-13', '0.2.8-12', '0.2.8-11',
            '0.2.8-7', '0.2.8-5', '0.2.8-4', '0.2.8-3', '0.2.8-2', '0.2.8-1', '0.2.8', '0.2.7-6', '0.2.7-5', '0.2.7-4',
            '0.2.7-3', '0.2.7-2', '0.2.7-1', '0.2.7', '0.2.6-14', '0.2.6-13', '0.2.6-12', '0.2.6-11', '0.2.6-10',
            '0.2.6-9', '0.2.6-8', '0.2.6-7', '0.2.6-6', '0.2.6-5', '0.2.6-4', '0.2.6-3', '0.2.6-2', '0.2.6-1', '0.2.6',
            '0.2.5-7', '0.2.5-6', '0.2.5-5', '0.2.5-4', '0.2.5-3', '0.2.5-2', '0.2.5-1', '0.2.5', '0.2.4-7', '0.2.4-6',
            '0.2.4-5', '0.2.4-4', '0.2.4-3', '0.2.4-1', '0.2.4', '0.2.3-10', '0.2.3-9', '0.2.3-8', '0.2.3-7', '0.2.3-6',
            '0.2.3-5', '0.2.3-4', '0.2.3-3', '0.2.3-2', '0.2.3-1', '0.2.2-12', '0.2.2-11', '0.2.2-10', '0.2.2-9',
            '0.2.2-8', '0.2.2-7', '0.2.2-6', '0.2.2-5', '0.2.2-4', '0.2.2-3', '0.2.2-2', '0.2.2-1', '0.2.2', '0.2.1-12',
            '0.2.1-11', '0.2.1-10', '0.2.1-9', '0.2.1-8', '0.2.1-7', '0.2.1-6', '0.2.1-5', '0.2.1-4', '0.2.1-3',
            '0.2.1-2', '0.2.1-1', '0.2.1', '0.2.0-6', '0.2.0-5', '0.2.0-4', '0.2.0-3', '0.2.0-2', '0.2.0-1', '0.2.0',
            '0.1.28-1', '0.1.28', '0.1.27-2', '0.1.27-1', '0.1.27', '0.1.26', '0.1.25', '0.1.24', '0.1.23', '0.1.22',
            '0.1.21', '0.1.20-3', '0.1.20-2', '0.1.20-1', '0.1.20', '0.1.19', '0.1.18', '0.1.17', '0.1.16', '0.1.15',
            '0.1.14', '0.1.13-1', '0.1.13', '0.1.12', '0.1.11', '0.1.10', '0.1.9-1', '0.1.9', '0.1.8-3', '0.1.8-2',
            '0.1.8-1', '0.1.8', '0.1.7', '0.1.6', '0.1.5', '0.1.4', '0.1.3', '0.1.2', '0.1.1', '0.1.0']

untag_list = ['0.2.2-3', '0.2.2-2', '0.2.2-1', '0.2.2', '0.2.1-12', '0.2.1-11', '0.2.1-10', '0.2.1-9', '0.2.1-8',
              '0.2.1-7', '0.2.1-6', '0.2.1-5', '0.2.1-4', '0.2.1-3', '0.2.1-2', '0.2.1-1', '0.2.1', '0.2.0-6',
              '0.2.0-5', '0.2.0-4', '0.2.0-3', '0.2.0-2', '0.2.0-1', '0.2.0', '0.1.28-1', '0.1.28', '0.1.27-2',
              '0.1.27-1', '0.1.27', '0.1.26', '0.1.25', '0.1.24', '0.1.23', '0.1.22', '0.1.21', '0.1.20-3', '0.1.20-2',
              '0.1.20-1', '0.1.20', '0.1.19', '0.1.18', '0.1.17', '0.1.16', '0.1.15', '0.1.14', '0.1.13-1', '0.1.13',
              '0.1.12', '0.1.11', '0.1.10', '0.1.9-1', '0.1.9', '0.1.8-3', '0.1.8-2', '0.1.8-1', '0.1.8', '0.1.7',
              '0.1.6', '0.1.5', '0.1.4', '0.1.3', '0.1.2', '0.1.1', '0.1.0']
version_list = ['0.2.2-4', '0.1.10']
expected_list = ['0.2.1-12', '0.2.1-11', '0.2.1-10', '0.2.1-9', '0.2.1-8', '0.2.1-7', '0.2.1-6', '0.2.1-5', '0.2.1-4',
                 '0.2.1-3', '0.2.1-2', '0.2.1-1', '0.2.1', '0.2.0-6', '0.2.0-5', '0.2.0-4', '0.2.0-3', '0.2.0-2',
                 '0.2.0-1', '0.2.0', '0.1.28-1', '0.1.28', '0.1.27-2', '0.1.27-1', '0.1.27', '0.1.26', '0.1.25',
                 '0.1.24', '0.1.23', '0.1.22', '0.1.21', '0.1.20-3', '0.1.20-2', '0.1.20-1', '0.1.20', '0.1.19',
                 '0.1.18', '0.1.17', '0.1.16', '0.1.15', '0.1.14', '0.1.13-1', '0.1.13', '0.1.12', '0.1.11', '0.1.8-1',
                 '0.1.8', '0.1.7', '0.1.6', '0.1.5', '0.1.4', '0.1.3', '0.1.2', '0.1.1', '0.1.0']


def test_previous_deployed_outdated():
    result = test_untag_list_template.keep_deployed_version(tag_list=tag_list,
                                                            untag_list=untag_list,
                                                            version_list=version_list)

    assert result == expected_list
