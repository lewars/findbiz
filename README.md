# findbiz

# Quick Setup

Here are the steps to quickly set up `findbiz` and run it successfully.

```sh
make build
cat << EOF > config.yml
---
location:
  - 18.019615
  - -76.779832
key: Insert_Your_API_Key_Here
EOF
python ./findbiz.py 'general contractor'
```
