test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

combined_set = set(test_design_writers + test_scripters + reviewers + out_of_office_today)
all_testers = list(combined_set)

testers_only_write_scripts = sorted(set(test_scripters) - set(test_design_writers) - set(reviewers))

testers_at_work = sorted(set(all_testers) - set(out_of_office_today))

testers_write_review_scripts = sorted(set(test_design_writers) & set(test_scripters) & set(reviewers) & set(testers_at_work))

print(all_testers)
print(testers_only_write_scripts)
print(testers_at_work)
print(testers_write_review_scripts)
