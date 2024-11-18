#!/bin/bash

failed_tests=()

print_status_and_record () {
  local test_name=$1
  local result="$2"
  local expected="$3"
  if [ "$result" = "$expected" ]; then
    echo SUCCESS
  else
    failed_tests+=("$test_name")
    echo FAILED
  fi
  echo
}

####################################### TEST nl #######################################

result="$(python ../src/nl.py small_text.txt)"
expected="$(nl -b a small_text.txt)"
print_status_and_record "test nl: text: small_text.txt, input: file" "$result" "$expected"

result="$(python ../src/nl.py big_text.txt)"
expected="$(nl -b a big_text.txt)"
print_status_and_record "test nl: text: big_text.txt, input: file" "$result" "$expected"

result="$(cat small_text.txt | python ../src/nl.py)"
expected="$(cat small_text.txt | nl -b a)"
print_status_and_record "test nl: text: small_text.txt, input: stdin" "$result" "$expected"

result="$(cat big_text.txt | python ../src/nl.py)"
expected="$(cat big_text.txt | nl -b a)"
print_status_and_record "test nl: text: big_text.txt, input: stdin" "$result" "$expected"

####################################### TEST tail #######################################

result="$(python ../src/tail.py small_text.txt)"
expected="$(tail small_text.txt)"
print_status_and_record "test tail: text: small_text.txt, input: file" "$result" "$expected"

result="$(python ../src/tail.py big_text.txt)"
expected="$(tail big_text.txt)"
print_status_and_record "test tail: text: big_text.txt, input: file" "$result" "$expected"

result="$(python ../src/tail.py big_text.txt small_text.txt)"
expected="$(tail big_text.txt  small_text.txt)"
print_status_and_record "test tail: text: big_text.txt + small_text.txt, input: multi files" "$result" "$expected"

result="$(cat small_text.txt | python ../src/tail.py)"
expected="$(cat small_text.txt | tail -n 17)"
print_status_and_record "test tail: text: small_text.txt, input: stdin" "$result" "$expected"

result="$(cat big_text.txt | python ../src/tail.py)"
expected="$(cat big_text.txt | tail -n 17)"
print_status_and_record "test tail: text: big_text.txt, input: stdin" "$result" "$expected"

####################################### TEST wc #######################################

result="$(python ../src/wc.py small_text.txt)"
expected="$(wc small_text.txt)"
print_status_and_record "test tail: text: small_text.txt, input: file" "$result" "$expected"

result="$(python ../src/wc.py big_text.txt)"
expected="$(wc big_text.txt)"
print_status_and_record "test tail: text: big_text.txt, input: file" "$result" "$expected"

result="$(python ../src/wc.py big_text.txt small_text.txt)"
expected="$(wc big_text.txt small_text.txt)"
print_status_and_record "test tail: text: big_text.txt + small_text.txt, input: multi files" "$result" "$expected"

result="$(cat small_text.txt | python ../src/wc.py)"
expected="$(cat small_text.txt | wc)"
print_status_and_record "test tail: text: small_text.txt, input: stdin" "$result" "$expected"

result="$(cat big_text.txt | python ../src/wc.py)"
expected="$(cat big_text.txt | wc)"
print_status_and_record "test tail: text: big_text.txt, input: stdin" "$result" "$expected"

if [ ${#failed_tests[@]} -eq 0 ]; then
  echo "All tests succeeded!"
else
  echo "${#failed_tests[@]} tests failed:"
  (IFS=$'\n'; echo "${failed_tests[*]}")
  exit 1
fi
