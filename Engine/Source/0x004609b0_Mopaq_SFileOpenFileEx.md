---
offset: "0x004609b0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004609b0 — `Mopaq_SFileOpenFileEx`

- **Адрес (Offset):** `0x004609b0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004609b0
int32_t Blizzard::Mopaq::SFileOpenFileEx(System_SFile::ARCHIVEREC* handle, const char* name, const Blizzard::Util::Digest<16>& md5, uint32_t flags, IOMpqUnit** result) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004609b0 в IDA Pro / Ghidra
