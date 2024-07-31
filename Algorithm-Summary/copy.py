## 얕은 복사와 깊은 복사

### 1차원 리스트 
data = [1, 2, 3, 4]

# 얕은 복사
temp_graph = data

# 깊은 복사
import copy
temp_graph = copy.deepcopy(data)

temp_graph = data[:]

### 2차원 리스트
data = [[1, 2, 3], [4, 5, 6]]

# 얕은 복사
temp_graph = data

# 깊은 복사
import copy
temp_data = copy.deepcopy(data)

temp_data = [row[:] for row in data]
