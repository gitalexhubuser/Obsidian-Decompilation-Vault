---
offset: "0x004541d0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004541d0 — `Mopaq_SetMd5Callback`

- **Адрес (Offset):** `0x004541d0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/SFileArchives.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004541d0
void Blizzard::Mopaq::SetMd5Callback(bool (*callback)(void* context, const uint8_t* md5)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004541d0 в IDA Pro / Ghidra
