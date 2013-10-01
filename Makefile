nanopb: proto
	python libs/nanopb/generator/nanopb_generator.py -s max_size:100 -f openxc.options gen/cpp/openxc.pb

proto: openxc.proto
	@mkdir -p gen/java
	@mkdir -p gen/python
	@mkdir -p gen/cpp
	protoc -I . -I gen -ogen/cpp/openxc.pb --python_out=gen/python --java_out=gen/java $?

all: nanopb proto
