from telethon import TelegramClient 
import logging 
import time  
  
  
openai_key = "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"
api_id = "1125689" 
  
api_hash = "4772d1792ed194020a8fb06a91ffb8fa" 
  
bot_token = "5877600853:AAGzETfRpALB0tFWpdN0OzP77oMtpqVwLGI" 
  
bot = TelegramClient("mugal", api_id, api_hash 
  ).start(bot_token = bot_token)