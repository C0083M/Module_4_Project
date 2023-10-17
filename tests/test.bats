#!/usr/bin/env bats


@test "Test when code is uploaded to main branch" {
  git clone https://github.com/bats-core/bats-core.git

  cd bats-core

  ./install.sh $HOME

  $HOME/bin/bats your_test_file.bats

  [ "$status" -eq 0 ]

  [ "$output" = "Expected Output" ]
}
