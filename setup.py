from setuptools import setup, find_packages

setup(
    name="Chatbot",
    version="0.1",
    packages=find_packages(),
    description="A Python chatbot project",
    author="Harman",
    install_requires=[
        "streamlit",
        "pandas",
        "matplotlib",
        "transformers"
    ],
)
