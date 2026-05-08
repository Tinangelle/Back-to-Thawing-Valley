# 开发日志源文件

> 每条日志在中文段之后使用 `@en`、`@fr` 分别写英文与法文。同一篇内三种语言的结构保持一致。  
> 更新后运行：`python tools/update_devlog.py`

## **2025年九月**

### **2025-09-17**

#### **标题：Demo战略定型与开场方案确立**

* **内容**：
  * **Demo战略**：采用“序章 + 花絮”模式，主体为沉浸式开局，结尾附带Meta风格的“杀青梗”。
  * **动画方案**：确定“精美定格插画 + 引擎动画”的混合模式，平衡艺术感与成本。
  * **引导哲学**：推行“给予工具，然后放手”，实现即时满足与情感驱动的种地引导。
  * **工作流**：确认“原型美术”工作流，先使用商用授权资源，后续再行替换。
* **备注**：正式启动《公开Demo开发计划 V1.0》。

@en
#### **Title: Demo strategy and opening approach locked in**

* **Content:**
  * **Demo structure:** A "prologue + extras" format—an immersive opening as the main beat, closing with a meta-style "wrap gag."
  * **Animation mix:** Freeze-frame style art plus in-engine animation to balance craft and production cost.
  * **Onboarding philosophy:** "Give tools, then let go"—immediate gratification plus emotion-led farming guidance.
  * **Pipeline:** "Prototype art" workflow first, using licensed commercial assets with planned replacement later.
* **Note:** Kick-off of the *Public Demo Development Plan v1.0*.

@fr
#### **Titre : Stratégie du démo et proposition d’ouverture validées**

* **Contenu :**
  * **Structure du démo :** mode « prologue + bonus » — ouverture immersive au centre, puis clin d’œil meta façon « générique de fin ».
  * **Animation :** combinaison illustrations figées soignées et animation moteur pour équilibre esthétique et coût.
  * **Guidage :** philosophie « donner les outils, puis lâcher prise » — satisfaction immédiate et tutorat des cultures porté par l’émotion.
  * **Workflow :** flux « art prototype » avec ressources sous licence en premier, remplacement envisagé ensuite.
* **Remarque :** lancement officiel du *plan de développement du démo public v1.0*.

### **2025-09-16**

#### **标题：钓鱼系统核心玩法与驱动模型**

* **内容**：
  * **玩法定型**：确立“听声辨位、单键反应”模式（灵感来自《动森》），支持闭眼游玩。
  * **奖励机制**：引入“斯金纳箱”理论，设计 D-S 级 Loot Table 及保底机制 (Pity Timer)。
  * **特色系统**：录入沉浸式通宵钓鱼、失物招领、举鱼游街及钓鱼日志等机制。
* **相关文件**：
  * 《钓鱼系统游戏设计文档 V1.0》
* **备注**：下一步需实现听觉循环原型及 Loot Table 数据结构。

@en
#### **Title: Fishing core loop and reward drivers**

* **Content:**
  * **Loop:** "Listen, aim, single-button react" (inspired by *Animal Crossing*)—playable eyes-free.
  * **Rewards:** Skinner-box framing with a D–S loot table and pity-timer safeguards.
  * **Features drafted:** Overnight immersive fishing, lost-and-found fish, parade carries, fishing journal hooks.
* **Related files:**
  * *Fishing Systems GDD v1.0*
* **Note:** Next—audio loop prototype plus loot-table data structures.

@fr
#### **Titre : Boucle principale et modèle récompenses de la pêche**

* **Contenu :**
  * **Boucle :** « entendre, viser, une touche » (inspiré d’*Animal Crossing*) — jouable sans regarder l’écran.
  * **Récompenses :** cadre type Skinner avec table de butin rang D–S et timer de pity.
  * **Systèmes :** pêche immersive de nuit, poissons trouvailles, présentation en défilé, carnet de pêche esquissés.
* **Fichiers :**
  * *GDD système pêche v1.0*
* **Remarque :** ensuite — prototype de boucle audio et structures données pour tables de loot.

### **2025-09-15**

#### **标题：核心设计哲学与风险评估**

* **内容**：
  * **哲学基调**：确立“心理避难所”地位，强调 NPC 无条件关怀，避免功利性。
  * **NPC 机制**：NPC 模式定义为世界的“基础自动运转模式”，玩家是社区发展的“催化剂”。
  * **叙事方向**：定性为“感情流”驱动，宏大背景采用“轻拿轻放”的碎片化叙事。
  * **高风险处理**：放弃内置现实书籍，放弃复杂动态模拟系统，AI 接入转向独立的实验分支计划。
* **备注**：集中精力打造纯手工、高质量的 MVP 核心体验。

@en
#### **Title: Core design pillars and risk triage**

* **Content:**
  * **Tone:** Position the game as a "psychological refuge"—NPC care without transactional grind frames.
  * **NPC paradigm:** NPCs embody the world's baseline rhythms; the player catalyzes community growth.
  * **Story:** Emotion-forward beats with "light-touch" fragmentation for lore-scale backdrops.
  * **Risks cut:** Drop embedded real-world books and heavy systemic simulation; sandbox AI experiments move to an isolated branch.
* **Note:** Focus resources on handcrafted, premium MVP pillars.

@fr
#### **Titre : Philosophie centrale et évaluation des risques**

* **Contenu :**
  * **Ton :** « refuge psychologique » — attention des PNJ sans logique trop utilitaire du joueur.
  * **PNJ :** rythmes de monde autonomes ; le joueur agit comme catalyseur du village.
  * **Narratif :** moteurs émotionnels, lore vaste distillé par touches légères.
  * **Risques évité :** pas de livres réels embarqués ni simulation systémique trop lourde ; l’IA expérimentale sur branche séparée.
* **Remarque :** concentrer l’équipe sur un MVP artisanal et de haute qualité.

### **2025-09-13**

#### **标题：核心 NPC（爷爷与奶奶）深度塑造**

* **内容**：
  * **爷爷 (Grandpa)**：身份定为“奇怪的拾荒者”，核心创伤为幸存者内疚，通过“弱链接误导 -> 强链接揭示”登场。
  * **奶奶 (Grandma)**：身份定为“故事讲述者”，代表“创伤后成长”，通过听故事解锁隐藏游戏机制。
* **备注**：确立了爷爷重新拿起鱼竿作为自我和解的象征。

@en
#### **Title: Core NPC archetypes—grandfather and grandmother**

* **Content:**
  * **Grandfather:** Oddball scavenger; survivor guilt anchors him via "weak misleading ties leading to resilient reveals."
  * **Grandmother:** Story keeper standing for post-traumatic growth; hearing tales unlocks hidden mechanics.
* **Note:** Fishing rod returned as emblem of reconciliation for Grandfather.

@fr
#### **Titre : PNJ centraux — grand-père et grand-mère**

* **Contenu :**
  * **Grand-père :** chiffonnier décalé ; culpabilité du survivant via fausses pistes puis révélation forte du lien réel.
  * **Grand-mère :** conteuse incarne la résilience ; écouter ses récits débloque des mécaniques cachées.
* **Remarque :** le grand-père reprend la pêche comme symbole de réconciliation intérieure.

### **2025-09-04**

#### **标题：玩家组件重构与高级拾取系统**

* **内容**：
  * **架构重构**：将工具管理与交互逻辑从 player.gd 剥离至 Hand.gd。
  * **拾取系统**：实现自动拾取（资源类）与手动拾取（作物类）双模式。
  * **调试工具**：创建 GM 命令（Z 键）实现时间暂停/继续。
* **相关文件**：
  * player.gd, Hand.gd, InventoryManager.gd, WoodPickup.gd
* **备注**：后续将进行地图“灰盒”搭建及镜头缩放功能开发。

@en
#### **Title: Player refactor and advanced pickups**

* **Content:**
  * **Architecture:** Tool orchestration/interaction peeled from player.gd into Hand.gd.
  * **Pickups:** Auto collect for resources versus manual gathers for crops.
  * **Debug:** GM shortcut (Z) toggles time pause/play.
* **Related files:**
  * player.gd, Hand.gd, InventoryManager.gd, WoodPickup.gd
* **Note:** Up next—greybox mapping pass plus camera zoom tooling.

@fr
#### **Titre : Refactor joueur et ramassages avancés**

* **Contenu :**
  * **Architecture :** outils et interactions extraits de `player.gd` vers `Hand.gd`.
  * **Ramassage :** auto pour ressources, manuel pour cultures.
  * **Debug :** raccourci MJ (touche Z) pour pause / reprise du temps.
* **Fichiers :**
  * player.gd, Hand.gd, InventoryManager.gd, WoodPickup.gd
* **Remarque :** puis greyboxing de carte et fonction zoom caméra.

### **2025-09-03**

#### **标题：后期动机困境与“克拉克森农场”模型**

* **内容**：
  * **叙事理论**：提出“攀登者的回望”，利用马斯洛需求层次引导后期目标转向社区贡献。
  * **终局方案**：引入规则迥异的新环境，玩家角色从“实干家”转变为“投资人”。
  * **高级机制**：构思“石匠的苏醒”（系统解锁包装）与“轮回者的馈赠”（二周目叙事化）。

@en
#### **Title: Late-game motivation and a "Clarkson's Farm"-style pivot**

* **Content:**
  * **Story theory:** Climber's hindsight—Maslow scaffolding nudges endgame goals toward community contribution.
  * **Late arc:** Alternate ruleset biome where the Delegate shifts builder-operator to steward-investor.
  * **High-tier hooks:** Stonemason awakening (fiction for system gates) plus cycle-gifter beats for NG+ narration.

@fr
#### **Titre : Motivation fin de jeu et modèle façon Clarkson**

* **Contenu :**
  * **Narratif :** regard du grimpeur — pyramide de Maslow pour orienter les objectifs tardifs vers la communauté.
  * **Fin de boucle :** nouveau cadre avec règles différentes ; passage de « généraliste terrain » à « investisseur stratège ».
  * **Hooks :** éveil du tailleur de pierre (habillage des déverrouillages), don du cycliste pour une narration new game plus.

### **2025-09-02**

#### **标题：核心循环闭合与交互标准化**

* **内容**：
  * **核心循环**：实现出货箱 (ShippingBin) 与日结算面板 (EndOfDayReport)。
  * **UI 架构**：升级 UIManager 为全局单例，与场景 HUD 解耦。
  * **接口规范**：统一所有被交互对象的函数签名。
* **相关文件**：
  * ShippingBin.gd, ui_manager.tscn, EndOfDayReport.gd

@en
#### **Title: Core loop closure & interaction normalization**

* **Content:**
  * **Economy beats:** Shipping bin plus end-of-day report UI.
  * **UI layer:** Promoted UIManager singleton decouples scene HUDs.
  * **Contracts:** Standard hit/interact signatures everywhere.
* **Related files:**
  * ShippingBin.gd, ui_manager.tscn, EndOfDayReport.gd

@fr
#### **Titre : Boucle principale fermée et interactions normalisées**

* **Contenu :**
  * **Boucle :** bac d’expédition et tableau de bilan journalier (`EndOfDayReport`).
  * **UI :** `UIManager` en singleton découple les HUD par scène.
  * **Interfaces :** signature unique pour tous les interactables.
* **Fichiers :**
  * ShippingBin.gd, ui_manager.tscn, EndOfDayReport.gd

### **2025-09-01**

#### **标题：项目架构重构与全局事件系统**

* **内容**：
  * **功能拆分**：将 FarmManager.gd 拆解为职责明确的 FarmingManager.gd。
  * **事件总线**：建立基于信号的 UIManager 全局 UI 事件系统。
  * **场景树升级**：优化 Main -> World + UI 的顶层结构，启用 Y-Sort。
* **相关文件**：
  * FarmingManager.gd, UIManager.gd

@en
#### **Title: Project architecture split & UI event backbone**

* **Content:**
  * **Splits:** FarmManager becomes focused FarmingManager.
  * **Events:** Signal-driven global UI broadcasting via UIManager.
  * **Scene graph:** Cleaner Main branch into World versus UI overlays with Y-sort.
* **Related files:**
  * FarmingManager.gd, UIManager.gd

@fr
#### **Titre : Refonte architecture et bus d’événements UI**

* **Contenu :**
  * **Découpe :** `FarmManager.gd` scindé en `FarmingManager.gd`.
  * **Bus :** signaux pour les évènements globaux traités dans `UIManager`.
  * **Scène :** structure Main → monde + couches UI ; tri Y-sort actif.
* **Fichiers :**
  * FarmingManager.gd, UIManager.gd

## **2025年八月**

### **2025-08-31**

#### **标题：系统架构搭建与第一个 Gameplay Loop**

* **内容**：
  * **单例模式**：创建 SeasonManager（中央时钟）与 PlayerStats（数据中心）。
  * **交互模型**：利用 RayCast2D 建立通用的 hit(tool) 交互接口。
  * **资源反馈**：实现带磁力吸附效果的掉落物。
* **相关文件**：
  * SeasonManager.gd, PlayerStats.gd, Tree.tscn, WoodPickup.tscn

@en
#### **Title: Architecture bootstrap and first gameplay loop**

* **Content:**
  * **Singleton services:** SeasonManager time hub plus PlayerStats data hub.
  * **Interactions:** Universal RayCast2D `hit(tool)` pattern.
  * **Loot feel:** Drops with magnetic ease-in feedback.
* **Related files:**
  * SeasonManager.gd, PlayerStats.gd, Tree.tscn, WoodPickup.tscn

@fr
#### **Titre : Pose de l’architecture et première boucle de jeu**

* **Contenu :**
  * **Singletons :** `SeasonManager` (horloge) et `PlayerStats` (centralisation des stats joueur).
  * **Gameplay :** `RayCast2D` pour interface générique `hit(tool)`.
  * **Récompenses visuelles :** drops avec aimantations courtes au ramassage.
* **Fichiers :**
  * SeasonManager.gd, PlayerStats.gd, Tree.tscn, WoodPickup.tscn

### **2025-08-30**

#### **标题：地图瓦片替换与四季变换功能**

* **内容**：
  * **资源更新**：创建全新 TileSet 资源并完成导入设置。
  * **季节动态**：通过 change_season 函数动态切换 TileMapLayer 的 tile_set。
* **备注**：修复了检查器未分配资源及函数名拼写错误。

@en
#### **Title: Tile refresh and seasonal map swaps**

* **Content:**
  * **Assets:** Built fresh TileSets with clean import presets.
  * **Seasons:** `change_season()` hot-swaps TileMapLayer tile_sets at runtime.
* **Note:** Fixed inspector dangling resources and typoed function identifiers.

@fr
#### **Titre : Tuiles carte et métamorphoses saisonnières**

* **Contenu :**
  * **Assets :** nouveau TileSet configuré jusqu’aux réglages d’importation.
  * **Saisons :** fonction `change_season()` commute `tile_set` des `TileMapLayer`.
* **Remarque :** correctifs inspections (ressources manquantes et noms de fonctions incorrects).

### **2025-08-28**

#### **标题：渲染技术研讨与 AI 控制**

* **内容**：
  * **视觉风格**：探讨伪 3D 轴测投影技术在 Godot 中的实现。
  * **成本控制**：决定将 AI 交互局限在特定区域（Area2D），以控制 API 调用成本。

@en
#### **Title: Rendering research and gated AI interplay**

* **Content:**
  * **Look:** Prototyping pseudo-isometric layering inside Godot.
  * **Cost control:** Anchor AI chatter to scripted Area2D pockets to conserve API budgets.

@fr
#### **Titre : Étude rendu et contrôle de l’IA**

* **Contenu :**
  * **Style :** expérimenter une fausse 3D isométrique via Godot.
  * **Coûts :** interactions IA cloisonnées par zones Area2D pour limiter les appels externes.

### **2025-08-27**

#### **标题：任务系统闭环与 UI 稳定性重构**

* **内容**：
  * **数据驱动**：任务系统升级为以 ID 为键的字典结构，实现 UI-数据解耦。
  * **坐标校准**：通过三步翻译流程修复 TileMap 交互偏移。
  * **UI 调试**：利用“远程”场景树修复了 ScrollContainer 布局难题。
* **备注**：解决了任务列表文字不换行及尺寸计算错误。

@en
#### **Title: Quest data closure plus UI stabilization**

* **Content:**
  * **IDs:** Tasks map by dictionary keys separating UI clones from authoring data.
  * **Coords:** Triple translation pass fixes TileMap aim offsets when selecting tiles.
  * **UI debug:** Remote scene tree helped tame ScrollContainers.
* **Note:** Wrapped text + layout measurement bugs cleared for quest roster.

@fr
#### **Titre : Quêtes data-driven et refonte fiabilité UI**

* **Contenu :**
  * **Données :** registre de quêtes par ID découpé de l’UI.
  * **Coords :** décalages TileMap corrigés par pipeline de trois translations.
  * **Debug UI :** arbre distant pour débloquer `ScrollContainer`.
* **Remarque :** retours à la ligne texte mesures corrigées sur la liste de quêtes.

### **2025-08-26**

#### **标题：万能手账 UI 重构与脚本清理**

* **内容**：
  * **职责剥离**：UI 更新逻辑从 World 移至 Notebook.gd。
  * **对话修复**：解决了因缺少 "start" 标题导致的对话框无法显示问题。
* **相关文件**：
  * Notebook.gd, World.gd

@en
#### **Title: Journal UI refactor**

* **Content:**
  * **Ownership:** Notebook.gd absorbs UI syncing that lived on World before.
  * **Dialog:** Restored Dialogue Manager passages missing the `start` title.
* **Related files:**
  * Notebook.gd, World.gd

@fr
#### **Titre : Refonte carnet tout-en-un et nettoyage scripts**

* **Contenu :**
  * **Séparation :** logique UI déplacée de `World` vers `Notebook.gd`.
  * **Dialogue :** correctif des scènes sans titre `start`.
* **Fichiers :**
  * Notebook.gd, World.gd

### **2025-08-25**

#### **标题：动态手账系统与像素艺术配置**

* **内容**：
  * **多标签设计**：基于 TabContainer 实现 Task 与 Social 页面。
  * **动态填充**：实现根据 WorldState 动态生成 TaskItem 实例。
  * **视觉优化**：配置项目为 CanvasItems 拉伸模式，确保像素清晰。
* **相关文件**：
  * Notebook.tscn, TaskItem.tscn, WorldState.gd

@en
#### **Title: Dynamic journal notebooks + crisp pixel prefs**

* **Content:**
  * **Tabs:** TabContainer juggling Task versus Social canvases.
  * **Hydration:** Spawns TaskItem clones from runtime WorldState.
  * **Rendering:** CanvasItems stretch presets protecting pixel fidelity.
* **Related files:**
  * Notebook.tscn, TaskItem.tscn, WorldState.gd

@fr
#### **Titre : Agenda dynamique et config pixel-perfect**

* **Contenu :**
  * **Onglets :** TabContainer séparant tâches et social.
  * **Contenu vivant :** instanciations `TaskItem` pilotées par `WorldState`.
  * **Pixels :** mode d’étirement CanvasItems pour garder une image nette.
* **Fichiers :**
  * Notebook.tscn, TaskItem.tscn, WorldState.gd

### **2025-08-24**

#### **标题：NPC 架构模板化与剧情衔接**

* **内容**：
  * **通用大脑**：创建 NPC_Base 作为所有角色的逻辑基座。
  * **序章实现**：通过代码实例化女巫角色，利用信号实现无缝剧情。
* **相关文件**：
  * NPC_Base.gd, Witch.gd, World.gd

@en
#### **Title: NPC template spine and scripted prologue stitches**

* **Content:**
  * **Base class:** NPC_Base houses shared brain logic across cast.
  * **Prologue beat:** Scripted witch spawn + signal bridges for seamless vignettes.
* **Related files:**
  * NPC_Base.gd, Witch.gd, World.gd

@fr
#### **Titre : Patron NPC et mise en orbite narratives**

* **Contenu :**
  * **Socle commun :** `NPC_Base.gd` porte les comportements génériques du casting.
  * **Prologue :** sorcière spawnée depuis le code reliée aux signaux narration.
* **Fichiers :**
  * NPC_Base.gd, Witch.gd, World.gd

### **2025-08-23**

#### **标题：对话系统升级与农场 MVP 实装**

* **内容**：
  * **插件接入**：采用 "Dialogue Manager" 插件，实现数据与内容分离。
  * **玩法闭环**：完成“开垦-播种-生长-收获”的完整农场循环。
* **相关文件**：
  * DialogueManager, WorldState.gd

@en
#### **Title: Dialogue Manager integration and farming MVP shipped**

* **Content:**
  * **Tooling:** Dialogue Manager cleanly splits copy from logic.
  * **Loop MVP:** Till, plant, grow, harvest—full slice live.
* **Related files:**
  * Dialogue Manager plugin assets, WorldState.gd

@fr
#### **Titre : Dialogue Manager et boucle ferme MVP**

* **Contenu :**
  * **Outils :** plugin Dialogue Manager — données narration séparées du code.
  * **Boucle :** labour, semis, croissance, récolte totalisés.
* **Fichiers :**
  * Dialogue Manager, WorldState.gd

### **2025-08-22**

#### **标题：季节性节日构思与伦理系统**

* **内容**：
  * **节日设计**：构思了依偎之夜（春）、湖上花火节（夏）、流浪者之夜（秋）。
  * **养殖伦理**：引入“命名契约”与“情感投资”机制，确立人道底线。
  * **社交锁**：引入深度对话解锁好感度进阶，拒绝无限送礼模式。

@en
#### **Title: Seasonal festivals drafted plus husbandry ethics**

* **Content:**
  * **Events:** Tender Night spring, lakeside fireworks summer, Voyager Night autumn.
  * **Livestock ethos:** Naming pacts plus emotional stewardship ground humane guardrails.
  * **Relationships:** Friendship tiers unlocked through meaningful dialogue—not endless gifting bots.

@fr
#### **Titre : Festivals saisonniers et éthique d’élevage**

* **Contenu :**
  * **Festivals :** Nuit enlacée (printemps), feux lacustres (été), Nuit des voyageurs (automne).
  * **Élevage :** pactes des noms investissement sentimental pour bornes bienveillantes.
  * **Amitiés :** étapes après dialogues riches — pas d’excès de loot cadeaux.

### **2025-08-21**

#### **标题：动画系统升级与纸娃娃结构**

* **内容**：
  * **换装支持**：重构动画为分层的 Body 与 Outfit 结构。
  * **NPC 交互**：实现第一个完整 NPC（奶奶）的互动感应与对话请求。
* **相关文件**：
  * Grandma.tscn, AnimatedSprite2D

@en
#### **Title: Animation stack uplift and paper doll layers**

* **Content:**
  * **Dressing pipeline:** Animated bodies split outfit slots for mix-and-match.
  * **NPC beat:** Grandma gets first holistic interact + greeting dialogue probes.
* **Related files:**
  * Grandma.tscn, AnimatedSprite2D setups

@fr
#### **Titre : Animations couches et première interaction PNJ**

* **Contenu :**
  * **Couches corps / tenues :** refactoring pour combinaisons façon pantin.
  * **PNJ clé :** grand-mère – premier jeu complet boucle perception + proposition de dialogue.
* **Fichiers :**
  * Grandma.tscn, AnimatedSprite2D

### **2025-08-20**

#### **标题：核心交互原型建立**

* **内容**：
  * **系统整合**：实现“对话 -> 选择 -> 反馈 -> 自由移动”的完整体验。
  * **基础资产**：初步建立 TileMap 农田和 Player 移动物理系统。

@en
#### **Title: Core interaction sandbox established**

* **Content:**
  * **Flow:** Dialogue, branch choice, feedback, roam—full micro vertical slice wired.
  * **World scaffolding:** Starter farm TileMap terrain plus kinematic-ish player motion.

@fr
#### **Titre : Proto des interactions centraux**

* **Contenu :**
  * **Flux :** dialogue choix branches retours exploration libre assemblée.
  * **Contenu monde :** TileMap fermière initiale mouvement physique du joueur.
