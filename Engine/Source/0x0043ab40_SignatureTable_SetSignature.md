---
offset: "0x0043ab40"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileSignatures.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0043ab40 — `SignatureTable_SetSignature`

- **Адрес (Offset):** `0x0043ab40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileSignatures.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0043ab40
bool System_SFile::SignatureTable::SetSignature(const char* name, const Blizzard::Util::Digest<16>& md5) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0043ab40 в IDA Pro / Ghidra
