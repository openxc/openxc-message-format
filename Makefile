nanopb: proto
	make -C libs/nanopb/generator/proto
	python libs/nanopb/generator/nanopb_generator.py gen/cpp/openxc.pb -f openxc.options

proto: openxc.proto
	@mkdir -p gen/java
	@mkdir -p gen/python
	@mkdir -p gen/cpp
	protoc -I . -I gen -ogen/cpp/openxc.pb --python_out=gen/python --java_out=gen/java $?

all: nanopb proto
