
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.legacy.readers.web import SimpleWebPageReader


# 设置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "sk-xxxxx"

# 加载文档
# documents = SimpleDirectoryReader("/Users/liuowen/Workspace/python/aiops24-RAG-demo/demo/data/director/中兴云操作指南").load_data()
# 1. 读取网页内容
url = "https://mp.weixin.qq.com/s/Xr1SofPScylWK5pMiaLvNg"  # 替换为你要读取的网页URL
documents = SimpleWebPageReader().load_data([url])

# 创建索引
index = VectorStoreIndex.from_documents(documents)

# 创建查询引擎
query_engine = index.as_query_engine()

# 提问
response = query_engine.query("分词像是做什么")
print(response)

