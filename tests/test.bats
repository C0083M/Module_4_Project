#!/usr/bin/env bats


@test "Test when code is uploaded to master branch" {
  if [[ $EUID -ne 0 ]]; then
    sudo su
  fi

  git clone https://github.com/bats-core/bats-core.git

  cd bats-core

  ./install.sh /usr/local

  bats your_test_file.bats

  [ "$status" -eq 0 ]

  [ "$output" = "Expected Output" ]

  if [[ $EUID -eq 0 ]]; then
    exit
  fi
}
