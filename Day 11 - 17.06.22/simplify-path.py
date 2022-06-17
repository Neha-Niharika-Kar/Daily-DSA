# STRINGS - Medium

# Given a string path, which is an absolute path to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory and a double period '..' refers to the directory up a level.
# Any multiple consecutive slashes '//' are treated as a single slash '/'. 
# For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:
# 1. The path starts with a single slash '/'.
# 2. Any two directories are separated by a single slash '/'.
# 3. The path does not end with a trailing '/'.
# 4. The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

# Return the simplified canonical path.

 class Solution:
    def simplifyPath(self, path: str) -> str:
        rev = reversed(path.split('/'))
        res = []
        count = 0
        for i in rev:
            if i == '..':
                count += 1
            elif i == '.' or i == '':
                continue
            else:
                if count:
                    count -= 1
                    continue  
                res.append(i)      
        return '/'+'/'.join(i for i in reversed(res))
