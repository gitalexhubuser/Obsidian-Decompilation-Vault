---
offset: "0x0045a260"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0045a260 — `Mopaq_SFileAuthenticateArchiveEx`

- **Адрес (Offset):** `0x0045a260`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0045a260
bool Blizzard::Mopaq::SFileAuthenticateArchiveEx(System_SFile::ARCHIVEREC* handle, AuthResult* result, const uint8_t* modulus, uint32_t modulusSize, const uint8_t* exponent, uint32_t exponentSize, const char* salt) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0045a260 в IDA Pro / Ghidra
