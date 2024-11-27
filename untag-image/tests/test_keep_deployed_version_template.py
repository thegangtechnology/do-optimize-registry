tag_list = ['staging', 'develop', 'latest', '1.0.38', '1.0.37', '1.0.36', '1.0.35', '1.0.34']


def keep_deployed_version(tag_list=[], untag_list=[]):
    keep_list = []
    final_list = untag_list
    for tag in tag_list:
        if tag == "develop" or tag == "staging" or tag == "production" or tag == "latest":
            index_keep = tag_list.index(tag)
            for i in range(5):
                if tag_list[index_keep + i] not in keep_list:
                    keep_list.append(tag_list[index_keep + i])
    print(f"keep version list : {keep_list}")
    print(f"keep extra {len(keep_list)} versions")
    # remove keep version from untag list
    for keep_version in keep_list:
        if keep_version in untag_list:
            final_list.remove(keep_version)
    return final_list
