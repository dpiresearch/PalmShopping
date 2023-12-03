# 1. PalmShopping
Generate shopping links using Google Palm

## Overview
Program that calls the Google generative models to query for shopping products and produce links.  In this case, the query asks for recommendations of laptops from Amazon.com and associated urls.

## Pre-requisites
Make sure you generate your credentials and set the GOOGLE_API_CREDENTIALS env variable to point to it

## Execution
% python google_palm.py

## Issues
The links that show up right now all end in the same token.  For example, the Amazon links in the below sample somehow all end in B097556645 and obviously don't work.  However, if you try this on the Bard UI, the links work.

## Sample output

| Rank | Laptop | GPU | CPU | RAM | Screen Size | Storage | Price | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | [Acer Predator Triton 500 SE](https://www.amazon.com/Acer-Predator-Triton-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 16.0" | 1TB SSD | $2,799.99 | [Amazon](https://www.amazon.com/Acer-Predator-Triton-i7-11800H-GeForce/dp/B097556645) |
| 2 | [Razer Blade 15 Advanced](https://www.amazon.com/Razer-Blade-15-Advanced-Gaming/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 15.6" | 1TB SSD | $3,499.99 | [Amazon](https://www.amazon.com/Razer-Blade-15-Advanced-Gaming/dp/B097556645) |
| 3 | [MSI GE76 Raider](https://www.amazon.com/MSI-GE76-Raider-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3080 Laptop GPU | Intel Core i7-11800H | 16GB | 17.3" | 1TB SSD | $3,299.99 | [Amazon](https://www.amazon.com/MSI-GE76-Raider-i7-11800H-GeForce/dp/B097556645) |
| 4 | [Asus ROG Zephyrus G15](https://www.amazon.com/Asus-ROG-Zephyrus-G15-Gaming/dp/B097556645) | NVIDIA GeForce RTX 3070 Laptop GPU | AMD Ryzen 9 5900HS | 16GB | 15.6" | 1TB SSD | $2,499.99 | [Amazon](https://www.amazon.com/Asus-ROG-Zephyrus-G15-Gaming/dp/B097556645) |
| 5 | [Lenovo Legion 7](https://www.amazon.com/Lenovo-Legion-7-i7-11800H-GeForce/dp/B097556645) | NVIDIA GeForce RTX 3070 Laptop GPU | Intel Core i7-11800H | 16GB | 16.0" | 1TB SSD | $2,799.99 | [Amazon](https://www.amazon.com/Lenovo-Legion-7-i7-11800H-GeForce/dp/B097556645) |

# 2. Search Amazon
Generate shopping links that actually work using Google custom search

## Execution
% python search_amazon.py

## Output

Enter your amazon search string: iphone chargers

You entered: iphone chargers

- [Anker 3.3ft Premium Double-Braided Nylon Lightning ... - Amazon.com](https://www.amazon.com/Anker-Double-Braided-Lightning-Certified-Chargers/dp/B078NPDRHL)
- [iPhone Charger Super Fast Charging [ MFi Certified ... - Amazon.com](https://www.amazon.com/Charger%E3%80%90Apple-Certified%E3%80%91-Charger-Lightning-Compatible/dp/B08N128B76)
- [Long iPhone Charger Cable 10 Ft Lightning Apple ... - Amazon.com](https://www.amazon.com/iPhone-Charger-Cable-Charging-3Meter/dp/B07RB54XJ2)
- [YUNSONG [MFi Certified] iPhone Charger, 3Pack 6FT ... - Amazon.com](https://www.amazon.com/Charger-YUNSONG-Lightning-Charging-Compatible/dp/B07PHB491R)
- [Ceptics Safest Travel Adapter Kit, Dual USB for iPhone, Chargers ...](https://www.amazon.com/Adapter-Chargers-Perfect-Travelers-Ceptics/dp/B07L56F6WJ)
- [Qntry USB Wall Charger, [MFi Certified] iPhone ... - Amazon.com](https://www.amazon.com/Charger-Certified-Lightning-Charging-Compatible/dp/B09BCNY1XR)
- [Miady 2-Pack 10000mAh Dual USB Portable Charger ... - Amazon.com](https://www.amazon.com/Miady-10000mAh-Portable-Charger-Charging/dp/B07XFBN7HX)
- [iPhone Charger,Atill 5 Pack 3ft/3ft/3ft/6ft/10ft Lightning ... - Amazon.com](https://www.amazon.com/Charger-Atill-Lightning-Charging-Compatible/dp/B07WD26RBC)
- [Apple MagSafe Charger - Wireless Charger with Fast ... - Amazon.com](https://www.amazon.com/Apple-MHXH3AM-A-MagSafe-Charger/dp/B08L5NP6NG)
- [4 Pack [Apple MFi Certified] Apple Charging Cables ... - Amazon.com](https://www.amazon.com/Certified-Charging-Cables-Chargers-Lightning/dp/B09BNDR17R)

# 3. Vision Shop

App that helps you shop based on pictures.

## Usage

Navigate to https://huggingface.co/spaces/dpang/vision_shop

Enter a url to an image with objects you're interesting in buying.  Hit the 'shop' button
The App will generate links to Amazon related to the objects it sees.

## Example

Use the following url for the image

https://images.ctfassets.net/7rldri896b2a/4augh14at0OZJuEhbWF0av/09dd54fe6543a36f2832f79cc51adad1/spc-bathdecor.jpg

## Output

decorative arched wall mirror bathroom vanity with storage
- [HQiJun Wall Mirror Window Decorative Mirrors ... - Amazon.com](https://www.amazon.com/Decorative-Mirrors-Farmhouse-Entryway-Bathroom/dp/B09DCLQBLC?tag=dpang-20)
- [Maxpeuvon Kids Bathroom Mirror with Shelf, Entryway ... - Amazon.com](https://www.amazon.com/Maxpeuvon-Bathroom-Entryway-Organizer-Bedroom/dp/B0BX5Y4S4S?tag=dpang-20)
- [HQiJun Wall Mirror Window Decorative Mirrors Arched Farmhouse ...](https://www.amazon.com/HQiJun-Decorative-Farmhouse-Entryway-Bathroom/dp/B0BTSNP1SK?tag=dpang-20)
- [Wall-Mounted Vanity Mirrors Arched Wall Mirror ... - Amazon.com](https://www.amazon.com/Wall-Mounted-Decorative-Bathroom-Aluminum-Entryway/dp/B0CBRY4D3W?tag=dpang-20)
- [Amazon.com: OGCAU Wall Mounted Mirror for Bathroom, Arched ...](https://www.amazon.com/OGCAU-Bathroom-Decorative-Aluminum-Entryway/dp/B09QPFB1CF?tag=dpang-20)
- [AZODY Arched Window Wall Mirror with Shelf, 36''x24 ... - Amazon.com](https://www.amazon.com/AZODY-Hanging-Entryway-Decorative-Bathroom/dp/B0CK29MYXG?tag=dpang-20)
- [AZODY Arched Window Wall Mirror with Shelf, 36''x24 ... - Amazon.com](https://www.amazon.com/AZODY-Hanging-Entryway-Decorative-Bathroom/dp/B0CK25LG8W?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=AVN3V2XB4JWWR&tag=dpang-20)
- [Kate and Laurel Barnhardt Decorative Wooden Wall ... - Amazon.com](https://www.amazon.com/Kate-Laurel-Arendahl-Frameless-Inspired/dp/B0BCSVV5MX?tag=dpang-20)
- [Kate and Laurel Astora Modern Arched Wall Mirror, 18 ... - Amazon.com](https://www.amazon.com/Kate-Laurel-Midcentury-Storage-Display/dp/B092BNC3P3?tag=dpang-20)
- [Kate and Laurel Peyson Arched Wall Mirror with Shelf ... - Amazon.com](https://www.amazon.com/Kate-Laurel-Decorative-Storage-Glamorous/dp/B0B2369WJV?tag=dpang-20)



