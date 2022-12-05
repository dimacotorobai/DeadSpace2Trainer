godmode_array = [                                   # ------------- Godmode Shellcode -------------
    0x50,                                           #       push eax
    0x53,                                           #       push ebx
    0xB8, 0x99, 0x99, 0x99, 0x99,                   #       mov eax,{Module Base Address}
    0x8B, 0x80, 0x54, 0xD5, 0xC4, 0x01,             #       mov eax,[eax+deadspace2.exe+184D554]
    0x8B, 0x40, 0x18,                               #       mov eax,[eax+0x18]
    0x8B, 0x40, 0x2C,                               #       mov eax,[eax+0x2C]
    0x8B, 0x40, 0x0C,                               #       mov eax,[eax+0x0C]
    0x05, 0xE8, 0x00, 0x00, 0x00,                   #       add eax,0xE8
    0x89, 0xFB,                                     #       mov ebx,edi
    0x81, 0xC3, 0xE8, 0x00, 0x00, 0x00,             #       add ebx, 0xE8
    0x39, 0xD8,                                     #       cmp eax,ebx
    0x74, 0x0A,                                     #       je PLAYER
    0xF3, 0x0F, 0x11, 0x87, 0xE8, 0x00, 0x00, 0x00, #       movss [edi+0xE8],xmm0
    0xEB, 0x17,                                     #       jmp RETURN

                                                    # PLAYER:
    0x8B, 0x87, 0xE4, 0x00, 0x00, 0x00,             #       mov eax,[edi+0xE4]
    0x89, 0x87, 0xE8, 0x00, 0x00, 0x00,             #       mov [edi+0xE8],eax
    0xB8, 0x00, 0x00, 0x80, 0x3F,                   #       mov eax, 3F800000(1.00f)
    0x89, 0x87, 0xEC, 0x00, 0x00, 0x00,             #       mov [edi+0xEC],eax

                                                    # RETURN:
    0x5B,                                           #       pop ebx
    0x58,                                           #       pop eax
    0x68, 0x99, 0x99, 0x99, 0x99,                   #       push {Return Address}
    0xC3                                            #       ret
]
