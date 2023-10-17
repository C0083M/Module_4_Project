#!/usr/bin/env bats


local_install_dir="$HOME/bats-local"

@test "Test when code is uploaded to main branch" {
  git clone https://github.com/bats-core/bats-core.git "$local_install_dir"

  cd "$local_install_dir"

  ./install.sh "$local_install_dir"

  "$local_install_dir/bin/bats" your_test_file.bats

  [ "$status" -eq 0 ]

  [ "$output" = "Expected Output" ]
}
