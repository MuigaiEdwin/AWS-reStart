#!/bin/bash

echo "=============================="
echo "   STUDENT INFO CHECKER"
echo "=============================="

read -p "Enter your name: " name
read -p "Enter your age: " age
read -p "What course are you taking? " course

echo ""
echo "------ RESULTS ------"

echo "Hello, $name!"
echo "You are $age years old."
echo "You are currently studying: $course."

if [ $age -lt 18 ]; then
    echo "Status: You are a minor student."
else
    echo "Status: You are an adult student."
fi

echo "=============================="
echo " Script Finished Successfully"
echo "=============================="
