# motion_photo_extractor.py
Python scritp to extract the embeeded motion photo data (MPG) from samsung JPG files.

The script basically converts the binary file to HEX and looks up for the tag 4D6F74696F6E50686F746F5F44617461 that means "MotionPhoto_Data" in ASCII and splits it in two portions the JPG portion and the MPG portion.

;)
