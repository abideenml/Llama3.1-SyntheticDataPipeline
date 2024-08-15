from setuptools import setup, find_packages

setup(
    name="Llama",
    version="0.1",
    packages=find_packages(),
    author="abideenml",
    author_email="zaiinn440@gmail.com",
    description="LLama 3.1 synthetic data generation pipeline.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abideenml/llm.pth",
    install_requires=[
        "transformers",
        "langchain",
        "flash-attn",
        "bitsandbytes",
        "accelerate",
        "pytest",
        "black",
        "graphviz",
        "langgraph",
        "openai",
        "pandas",
        "tqdm",
    ],
    python_requires=">=3.8",
)