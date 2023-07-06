import urllib.request
import json


i: int = int(input('number of block?: '))
url = f"https://blockchain.info/block-height/{i}?format=json"

r = urllib.request.urlopen(url)
data = json.load(r)

print(data)

# {
    # 'blocks': [
        # {
            # 'hash': '0000000067a97a2a37b8f190a17f0221e9c3f4fa824ddffdc2e205eae834c8d7',
            # 'ver': 1, 
            # 'prev_block': '00000000841cb802ca97cf20fb9470480cae9e5daa5d06b4a18ae2d5dd7f186f', 
            # 'mrkl_root': 'ee1afca2d1130676503a6db5d6a77075b2bf71382cfdf99231f89717b5257b5b', 
            # 'time': 1231565995, 
            # 'bits': 486604799, 
            # 'next_block': [
                # '000000006f016342d1275be946166cff975c8b27542de70a7113ac6d1ef3294f'
            # ], 
            # 'fee': 0, 
            # 'nonce': 1901123894, 
            # 'n_tx': 1, 
            # 'size': 215, 
            # 'block_index': 20, 
            # 'main_chain': True, 
            # 'height': 20, 
            # 'weight': 860, 
            # 'tx': [
                # {
                    # 'hash': 'ee1afca2d1130676503a6db5d6a77075b2bf71382cfdf99231f89717b5257b5b', 
                    # 'ver': 1, 
                    # 'vin_sz': 1, 
                    # 'vout_sz': 1, 
                    # 'size': 134, 
                    # 'weight': 536, 
                    # 'fee': 0, 
                    # 'relayed_by': '0.0.0.0', 
                    # 'lock_time': 0, 
                    # 'tx_index': 3218703095362303, 
                    # 'double_spend': False, 
                    # 'time': 1231565995, 
                    # 'block_index': 20, 
                    # 'block_height': 20, 
                    # 'inputs': [
                        # {
                            # 'sequence': 4294967295, 
                            # 'witness': '', 
                            # 'script': '04ffff001d0120', 
                            # 'index': 0, 
                            # 'prev_out': {
                                # 'n': 4294967295, 
                                # 'script': '', 
                                # 'spending_outpoints': [
                                    # {
                                        # 'n': 0, 
                                        # 'tx_index': 3218703095362303
                                    # }
                                # ],
                                # 'spent': True, 
                                # 'tx_index': 0, 
                                # 'type': 0, 
                                # 'value': 0
                            # }
                        # }
                    # ], 
                    # 'out': [
                        # {
                            # 'type': 0, 
                            # 'spent': False, 
                            # 'value': 5000000000, 
                            # 'spending_outpoints': [], 
                            # 'n': 0, 
                            # 'tx_index': 3218703095362303, 
                            # 'script': '410408ab2f56361f83064e4ce51acc291fb57c2cbcdb1d6562f6278c43a1406b548fd6cefc11bcc29eb620d5861cb9ed69dc39f2422f54b06a8af4f78c8276cfdc6bac', 
                            # 'addr': '15ubjFzmWVvj3TqcpJ1bSsb8joJ6gF6dZa'
                        # }
                    # ]
                # }
             # ]
        # }
    # ]
# } 