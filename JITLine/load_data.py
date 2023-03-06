from my_util import *


def write_commit_id(data, target_file):
    file = open(target_file, "w")

    file.write("commit_id = ")
    file.write("[")
    for commit in data:
        file.write('"' + commit + '",')
    file.write("]")

    file.close()


def write_commit_message(data, target_file):
    file = open(target_file, "w")

    file.write("commit_message = ")
    file.write("[")
    for commit in data:
        file.write('"' + commit + '",')
    file.write("]")

    file.close()


def write_code_changes(data, target_file):
    file = open(target_file, "w")

    file.write("code_changes = ")
    file.write("[")
    for hunk in data:
        file.write("[")
        for line in hunk:
            file.write('{"added_code":[')
            for added_code in line.get("added_code"):
                file.write('"')
                file.write(added_code)
                file.write('", ')
            file.write("],")
            file.write('"removed_code":[')
            for removed_code in line.get("removed_code"):
                file.write('"')
                file.write(removed_code)
                file.write('", ')
            file.write("]},")
        file.write("],")
    file.write("]")

    file.close()


def write_pseudo_code(data, target_file, code_type="added_code"):
    for hunk_id, hunk in enumerate(data):
        for line_id, line in enumerate(hunk):
            if code_type == "added_code":
                file = open("./added_code/" + str(hunk_id) + "-" + str(line_id), "w")
                for added_code in line.get("added_code"):
                    file.write(added_code)
                    file.write("\n")
                file.close()
            elif code_type == "removed_code":
                file = open("./removed_code/" + str(hunk_id) + "-" + str(line_id), "w")
                for removed_code in line.get("removed_code"):
                    file.write(removed_code)
                    file.write("\n")
                file.close()


data = pickle.load(open("./data/" + "openstack" + "_train.pkl", "rb"))
write_commit_id(data[0][:8], "commit_id.py")
write_commit_message(data[2][:8], "commit_message.py")
write_code_changes(data[3][:8], "code_changes.py")
defect_commits = []
for i in range(len(data[0])):
    if data[1][i]:
        defect_commits.append(data[3][i])
write_code_changes(defect_commits[:8], "defect_changes.py")
write_pseudo_code([defect_commits[1]], "added_code.txt", "added_code")
write_pseudo_code([defect_commits[1]], "removed_code.txt", "removed_code")

# file = open('data/test.pkl', 'wb')
# pickle.dump(data, file)
# file.close()
# test = pickle.load(open('./data/test.pkl', 'rb'))
# print(test)

# dict = pickle.load(open('./data/'+'openstack'+'_dict.pkl','rb'))
# print(dict)

# data = pickle.load(open('../CC2Vec_Modified/data/openstack_train.pkl'))
# print(data)
# file = open('../CC2Vec_Modified/data/openstack_train.pkl', encoding="utf-8")
