---
offset: "0x00437470"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileSignatures.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00437470 — `SignatureTable_GetSignature`

- **Адрес (Offset):** `0x00437470`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileSignatures.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00437470
bool System_SFile::SignatureTable::GetSignature(const char* name, Blizzard::Util::Digest<16>* md5) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00437470 в IDA Pro / Ghidra
