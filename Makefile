.DEFAULT_GOAL := help
DAY ?= 1
PART ?= 1

.PHONY: run # Run specific day and part. Usage: DAY=[1-25] PART=[1-2] make run
run:
	@echo "Running script for day ${DAY} part ${PART}:"
	@echo
	@cd day${DAY} && python3 part${PART}.py

.PHONY: help # Print help screen
help:
	@echo
	@echo "\033[1m\033[7m                               \033[0m"
	@echo "\033[1m\033[7m ADVENT OF CODE SOLUTIONS 2020 \033[0m"
	@echo "\033[1m\033[2m\033[3m\033[7m     I've been a good boy!     \033[0m"
	@echo "\033[1m\033[7m                               \033[0m"
	@echo
	@echo "\033[0;33mEnvironment variables:"
	@printf "  \033[0;32m%-25s \033[0;0m%-60s Value: [ \033[0;35m%-2s\033[0;0m ]\n" "DAY" "Specify the day to run. Valid values: 1-25" "${DAY}"
	@printf "  \033[0;32m%-25s \033[0;0m%-60s Value: [ \033[0;35m%-2s\033[0;0m ]\n" "PART" "Specify the part to run. Valid values: 1,2" "${PART}"
	@echo
	@echo "\033[0;33mTargets:\033[0m"
	@grep -E '^\.PHONY: .* #' makefile | sed -E 's/^\.PHONY: (.*) # (.*)/"\1" "\2"/g' | xargs printf "  \033[0;32m%-25s \033[0;0m%s\n"
