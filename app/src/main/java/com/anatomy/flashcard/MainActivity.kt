package com.anatomy.flashcard

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateMapOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import com.anatomy.flashcard.data.DataManager
import com.anatomy.flashcard.data.ProgressManager
import com.anatomy.flashcard.data.QuizPreferences
import com.anatomy.flashcard.data.SubjectManager
import com.anatomy.flashcard.model.AnatomySystemType
import com.anatomy.flashcard.model.FlashcardDeck
import com.anatomy.flashcard.model.MindMapData
import com.anatomy.flashcard.model.QuizRecord
import com.anatomy.flashcard.model.QuizSet
import com.anatomy.flashcard.model.StudyProgress
import com.anatomy.flashcard.model.Subject
import com.anatomy.flashcard.model.SubjectViewMode
import com.anatomy.flashcard.ui.components.ImportDialog
import com.anatomy.flashcard.ui.screens.HomeScreen
import com.anatomy.flashcard.ui.screens.QuizScreen
import com.anatomy.flashcard.ui.screens.StudyScreen
import com.anatomy.flashcard.ui.screens.SubjectSelectScreen
import com.anatomy.flashcard.ui.screens.SystemHubScreen
import com.anatomy.flashcard.ui.theme.AnatomyFlashcardTheme

import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInHorizontally
import androidx.compose.animation.slideOutHorizontally
import androidx.compose.animation.togetherWith
import com.anatomy.flashcard.ui.motion.MotionSpecs

sealed class AppDestination {
    object SubjectSelect : AppDestination()
    data class Home(val subject: Subject) : AppDestination()
    data class SystemHub(val subject: Subject, val systemType: AnatomySystemType, val initialTab: Int = 0) : AppDestination()
    data class Study(val subject: Subject, val systemType: AnatomySystemType, val deck: FlashcardDeck) : AppDestination()
    data class Quiz(val subject: Subject, val systemType: AnatomySystemType, val quizSet: QuizSet) : AppDestination()

    fun depth(): Int = when (this) {
        is SubjectSelect -> 0
        is Home -> 1
        is SystemHub -> 2
        is Study, is Quiz -> 3
    }
}

class MainActivity : ComponentActivity() {

    private lateinit var dataManager: DataManager
    private lateinit var progressManager: ProgressManager
    private lateinit var quizPreferences: QuizPreferences
    private lateinit var subjectManager: SubjectManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        dataManager = DataManager(this)
        progressManager = ProgressManager(this)
        quizPreferences = QuizPreferences(this)
        subjectManager = SubjectManager(this)

        setContent {
            AnatomyFlashcardTheme {
                FlashcardApp(
                    dataManager = dataManager,
                    progressManager = progressManager,
                    quizPreferences = quizPreferences,
                    subjectManager = subjectManager
                )
            }
        }
    }
}

@Composable
fun FlashcardApp(
    dataManager: DataManager,
    progressManager: ProgressManager,
    quizPreferences: QuizPreferences,
    subjectManager: SubjectManager
) {
    var reloadTrigger by remember { mutableIntStateOf(0) }
    var showImportDialog by remember { mutableStateOf(false) }

    // 学科列表与视图模式状态
    var subjects by remember(reloadTrigger) { mutableStateOf(subjectManager.getSubjects()) }
    var viewMode by remember { mutableStateOf(subjectManager.getViewMode()) }

    // 默认进入学科选择大厅
    var destination by remember { mutableStateOf<AppDestination>(AppDestination.SubjectSelect) }

    val currentSubjectId = when (val d = destination) {
        is AppDestination.Home -> d.subject.id
        is AppDestination.SystemHub -> d.subject.id
        is AppDestination.Study -> d.subject.id
        is AppDestination.Quiz -> d.subject.id
        else -> "anatomy"
    }

    val currentUnits = remember(currentSubjectId, reloadTrigger) {
        dataManager.getUnitsForSubject(currentSubjectId)
    }

    // Dynamic reload based on currentUnits and reloadTrigger
    val decksMap = remember(currentUnits, reloadTrigger) {
        currentUnits.associateWith { dataManager.loadDeck(it) }.filterValues { it != null }.mapValues { it.value!! }
    }

    val quizSetsMap = remember(currentUnits, reloadTrigger) {
        currentUnits.associateWith { dataManager.loadQuizSet(it) }.filterValues { it != null }.mapValues { it.value!! }
    }

    val mindMapsMap = remember(currentUnits, reloadTrigger) {
        currentUnits.associateWith { dataManager.loadMindMap(it) }
    }

    // Progress Maps
    val deckProgressMap = remember(decksMap, reloadTrigger) {
        mutableStateMapOf<String, StudyProgress>().apply {
            decksMap.values.forEach { deck ->
                put(deck.id, progressManager.getProgress(deck.id))
            }
        }
    }

    val quizRecordMap = remember(quizSetsMap, reloadTrigger) {
        mutableStateMapOf<String, QuizRecord>().apply {
            quizSetsMap.values.forEach { quiz ->
                put(quiz.id, quizPreferences.getRecord(quiz.id))
            }
        }
    }

    Surface(modifier = Modifier.fillMaxSize()) {
        AnimatedContent(
            targetState = destination,
            transitionSpec = {
                val forward = targetState.depth() >= initialState.depth()
                if (forward) {
                    (slideInHorizontally(
                        initialOffsetX = { fullWidth -> fullWidth },
                        animationSpec = tween(durationMillis = 350, easing = MotionSpecs.EmphasizedDecelerate)
                    ) + fadeIn(animationSpec = tween(280)))
                        .togetherWith(
                            slideOutHorizontally(
                                targetOffsetX = { fullWidth -> -fullWidth / 3 },
                                animationSpec = tween(durationMillis = 350, easing = MotionSpecs.EmphasizedEasing)
                            ) + fadeOut(animationSpec = tween(240))
                        )
                } else {
                    (slideInHorizontally(
                        initialOffsetX = { fullWidth -> -fullWidth / 3 },
                        animationSpec = tween(durationMillis = 350, easing = MotionSpecs.EmphasizedDecelerate)
                    ) + fadeIn(animationSpec = tween(280)))
                        .togetherWith(
                            slideOutHorizontally(
                                targetOffsetX = { fullWidth -> fullWidth },
                                animationSpec = tween(durationMillis = 350, easing = MotionSpecs.EmphasizedEasing)
                            ) + fadeOut(animationSpec = tween(240))
                        )
                }
            },
            label = "AppScreenTransition"
        ) { dest ->
            when (dest) {
                is AppDestination.SubjectSelect -> {
                    SubjectSelectScreen(
                        subjects = subjects,
                        viewMode = viewMode,
                        onToggleViewMode = {
                            val newMode = if (viewMode == SubjectViewMode.GRID) SubjectViewMode.LIST else SubjectViewMode.GRID
                            viewMode = newMode
                            subjectManager.setViewMode(newMode)
                        },
                        onSelectSubject = { selectedSubject ->
                            subjectManager.setLastSelectedSubjectId(selectedSubject.id)
                            destination = AppDestination.Home(selectedSubject)
                        },
                        onAddSubject = { name, emoji, desc ->
                            val newSub = subjectManager.addSubject(name, emoji, desc)
                            subjects = subjectManager.getSubjects()
                        },
                        onUpdateSubject = { id, name, emoji, desc ->
                            subjectManager.updateSubject(id, name, emoji, desc)
                            subjects = subjectManager.getSubjects()
                        },
                        onUpdateSubjectEmoji = { id, newEmoji ->
                            subjectManager.updateSubjectEmoji(id, newEmoji)
                            subjects = subjectManager.getSubjects()
                        },
                        onDeleteSubject = { id ->
                            subjectManager.deleteSubject(id)
                            subjects = subjectManager.getSubjects()
                        }
                    )
                }

                is AppDestination.Home -> {
                    BackHandler {
                        destination = AppDestination.SubjectSelect
                    }
                    HomeScreen(
                        currentSubject = dest.subject,
                        systems = currentUnits,
                        decks = decksMap,
                        deckProgressMap = deckProgressMap,
                        quizSets = quizSetsMap,
                        quizRecords = quizRecordMap,
                        onSelectSystem = { sys ->
                            destination = AppDestination.SystemHub(dest.subject, sys, 0)
                        },
                        onSelectSystemTab = { sys, tab ->
                            destination = AppDestination.SystemHub(dest.subject, sys, tab)
                        },
                        onOpenImport = {
                            showImportDialog = true
                        },
                        onBackToSubjects = {
                            destination = AppDestination.SubjectSelect
                        }
                    )
                }

                is AppDestination.SystemHub -> {
                    BackHandler {
                        destination = AppDestination.Home(dest.subject)
                    }
                    val currentDeck = decksMap[dest.systemType]
                    val currentQuiz = quizSetsMap[dest.systemType]
                    val currentMindMap = mindMapsMap[dest.systemType]
                    val currentProgress = currentDeck?.let { deckProgressMap[it.id] } ?: StudyProgress(currentDeck?.id ?: "")
                    val currentRecord = currentQuiz?.let { quizRecordMap[it.id] }
                    val currentSession = currentQuiz?.let { quizPreferences.getSession(it.id) }

                    SystemHubScreen(
                        systemType = dest.systemType,
                        deck = currentDeck,
                        deckProgress = currentProgress,
                        quizSet = currentQuiz,
                        quizRecord = currentRecord,
                        quizSession = currentSession,
                        mindMap = currentMindMap,
                        initialTab = dest.initialTab,
                        onStartFlashcards = {
                            if (currentDeck != null) {
                                destination = AppDestination.Study(dest.subject, dest.systemType, currentDeck)
                            }
                        },
                        onStartQuiz = {
                            if (currentQuiz != null) {
                                destination = AppDestination.Quiz(dest.subject, dest.systemType, currentQuiz)
                            }
                        },
                        onBack = {
                            destination = AppDestination.Home(dest.subject)
                        }
                    )
                }

                is AppDestination.Study -> {
                    BackHandler {
                        destination = AppDestination.SystemHub(dest.subject, dest.systemType)
                    }
                    val progress = deckProgressMap[dest.deck.id] ?: progressManager.getProgress(dest.deck.id)
                    StudyScreen(
                        deck = dest.deck,
                        initialProgress = progress,
                        onSaveProgress = { newProgress ->
                            deckProgressMap[dest.deck.id] = newProgress
                            progressManager.saveProgress(newProgress)
                        },
                        onBack = {
                            destination = AppDestination.SystemHub(dest.subject, dest.systemType)
                        }
                    )
                }

                is AppDestination.Quiz -> {
                    val initialSession = remember(dest.quizSet.id, destination) {
                        quizPreferences.getSession(dest.quizSet.id)
                    }
                    BackHandler {
                        destination = AppDestination.SystemHub(dest.subject, dest.systemType)
                    }
                    QuizScreen(
                        quizSet = dest.quizSet,
                        initialSession = initialSession,
                        onSaveSession = { session ->
                            quizPreferences.saveSession(session)
                        },
                        onClearSession = {
                            quizPreferences.clearSession(dest.quizSet.id)
                        },
                        onFinishQuiz = { score, total, wrongIds ->
                            quizPreferences.saveAttempt(dest.quizSet.id, score, total, wrongIds)
                            quizPreferences.clearSession(dest.quizSet.id)
                            quizRecordMap[dest.quizSet.id] = quizPreferences.getRecord(dest.quizSet.id)
                        },
                        onBack = {
                            destination = AppDestination.SystemHub(dest.subject, dest.systemType)
                        }
                    )
                }
            }
        }

        // Show Import Dialog
        if (showImportDialog) {
            ImportDialog(
                importManager = dataManager.importManager,
                onDismiss = { showImportDialog = false },
                onImportSuccess = {
                    reloadTrigger++
                }
            )
        }
    }
}
