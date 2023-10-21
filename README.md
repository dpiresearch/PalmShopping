# PalmShopping
Generate shopping links using Google Palm

## Overview
Program that calls the Google Palm generative models to query for shopping products and produce links.  Example output video

## Pre-requisites
Make sure you generate your credentials and set the GOOGLE_API_CREDENTIALS env variable to point to it

## Execution
% python google_palm.py

## Sample output

| Rank | Laptop | GPU | CPU | RAM | Screen Size | Storage | Price | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | [Acer Predator Triton 500 SE](https://www.amazon.com/Acer-Predator-Triton-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 16.0" | 1TB SSD | $2,799.99 | [Amazon](https://www.amazon.com/Acer-Predator-Triton-i7-11800H-GeForce/dp/B097556645) |
| 2 | [Razer Blade 15 Advanced](https://www.amazon.com/Razer-Blade-15-Advanced-Gaming/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 15.6" | 1TB SSD | $3,499.99 | [Amazon](https://www.amazon.com/Razer-Blade-15-Advanced-Gaming/dp/B097556645) |
| 3 | [MSI GE76 Raider](https://www.amazon.com/MSI-GE76-Raider-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 17.3" | 1TB SSD | $3,299.99 | [Amazon](https://www.amazon.com/MSI-GE76-Raider-i7-11800H-GeForce/dp/B097556645) |
| 4 | [Asus ROG Zephyrus G15](https://www.amazon.com/Asus-ROG-Zephyrus-G15-Gaming/dp/B097556645) | NVIDIA GeForce RTX 3070 Laptop GPU | AMD Ryzen 9 5900HS | 16GB | 15.6" | 1TB SSD | $2,499.99 | [Amazon](https://www.amazon.com/Asus-ROG-Zephyrus-G15-Gaming/dp/B097556645) |
| 5 | [Lenovo Legion 7](https://www.amazon.com/Lenovo-Legion-7-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3070 Laptop GPU | Intel Core i7-11800H | 16GB | 16.0" | 1TB SSD | $2,799.99 | [Amazon](https://www.amazon.com/Lenovo-Legion-7-i7-11800H-GeForce/dp/B097556645) |

