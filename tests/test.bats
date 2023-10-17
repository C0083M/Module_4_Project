#!/usr/bin/env bats

@test "Test when code is uploaded to main branch" {
  run python3 index.py

  [ "$status" -eq 0 ]

  [ "$output" = "Expected Output" ]
}
