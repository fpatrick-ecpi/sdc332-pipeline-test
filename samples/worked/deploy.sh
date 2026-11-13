#!/bin/bash
target=$1
cd $target
echo "Deploying from" `pwd`
rm -rf $target/build/*
