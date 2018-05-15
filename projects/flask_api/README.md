API
===============
### 运行
python run.py

### 枚举值
```python
class TaskStatus:
    ONGOING = 1
    COMPLETED = 2
```

### 接口定义
#### 1. 创建任务

链接：

/task/api/createTask

HTTP POST

| 参数名称     | 含义                        | 示例           | 是否必填 |
| ----------- | -------------------------  | -------------  | ----    |
| task        | 任务名称                    | 'drink milk'     | 是      |
| priority    | 优先级                      | 1              | 是    |
| owner     | 所属者                    | 'cxx'            | 是    |

返回值： 

```json
{
"success": true,
"desc": "success",
"value": {
     "task": "milk",
     "priority": "1",
     "owner": "cxx",
     "status": "ONGOING"
       }
}
``` 

备注：  
1. 新增任务状态默认为 "ONGOING";   
2. owner 必须在register_user表中。


#### 2. 获取任务信息

链接：

/task/api/getTask

HTTP GET

| 参数名称     | 含义           | 示例          | 是否必填 |
| ----------- | --------------| -----------   | ---- |
| task        | 任务名称       | 'drink milk'     | 是    |


返回值：

```json
{
"success": true,
"desc": "success",
"value": {
     "task": "milk",
     "priority": "1",
     "owner": "cxx",
     "status": "ONGOING"
       }
}
``` 


#### 3. 获取任务列表

链接：
/task/api/getTaskList

HTTP GET

| 参数名称     | 含义           | 示例          | 是否必填 |
| ----------- | --------------| -----------   | ---- |
| 无        | /     | /    | /   |


返回值：

```json
{
"success": true,
"desc": "success",
"value": [
{
"task": "milk",
"priority": "1",
"owner": "",
"status": "ONGOING"
},
{
"task": "test-d017e",
"priority": "7",
"owner": "",
"status": "COMPLETED"
},
{
"task": "test-6a3e9",
"priority": "8",
"owner": "cxx",
"status": "ONGOING"
},
{
"task": "test399a5",
"priority": "9",
"owner": "",
"status": "ONGOING"
}
]
}
```


#### 4.更改任务状态  

链接：
/task/api/editTask  

HTTP POST

| 参数名称     | 含义                        | 示例           | 是否必填 |
| ----------- | -------------------------  | -------------  | ----    |
| task        | 任务名称                    | 'drink milk'     | 是      |
| status    | 状态                     | 2              | 是    |


返回值：

```json
{
"success": true,
"desc": "success",
"value": {
     "task": "milk",
     "priority": "1",
     "owner": "cxx",
     "status": "COMPLETED"
       }
}
``` 

