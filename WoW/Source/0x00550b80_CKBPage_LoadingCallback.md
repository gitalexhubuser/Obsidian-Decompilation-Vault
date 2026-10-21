---
offset: "0x00550b80"
module: "WoW/Source"
file: "WoW/Source/Ui/KnowledgeBase.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00550b80 — `CKBPage_LoadingCallback`

- **Адрес (Offset):** `0x00550b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/KnowledgeBase.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00550b80
bool CKBPage::LoadingCallback(void* param, const char* data, uint32_t size, bool done, HTTPError::ErrorCode error) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00550b80 в IDA Pro / Ghidra
