/*
 * File: programeditor.js
 * Created on Mon May 27 19:13:07 PDT 2019 by java2js
 * --------------------------------------------------
 * This file was generated mechanically by the java2js utility.
 * Permanent edits must be made in the Java file.
 */

define([ "jslib",
         "edu/stanford/cs/java2js",
         "edu/stanford/cs/jseditor",
         "java/awt",
         "java/lang",
         "java/util",
         "javax/swing" ],

function(jslib,
         edu_stanford_cs_java2js,
         edu_stanford_cs_jseditor,
         java_awt,
         java_lang,
         java_util,
         javax_swing) {

/* Imports */

var inheritPrototype = jslib.inheritPrototype;
var newArray = jslib.newArray;
var toInt = jslib.toInt;
var toStr = jslib.toStr;
var JSCanvas = edu_stanford_cs_java2js.JSCanvas;
var JSErrorDialog = edu_stanford_cs_java2js.JSErrorDialog;
var JSImage = edu_stanford_cs_java2js.JSImage;
var EditorMode = edu_stanford_cs_jseditor.EditorMode;
var HighlighterKey = edu_stanford_cs_jseditor.HighlighterKey;
var JSEditor = edu_stanford_cs_jseditor.JSEditor;
var Marker = edu_stanford_cs_jseditor.Marker;
var BorderLayout = java_awt.BorderLayout;
var Color = java_awt.Color;
var Dimension = java_awt.Dimension;
var FontMetrics = java_awt.FontMetrics;
var Graphics = java_awt.Graphics;
var Point = java_awt.Point;
var Rectangle = java_awt.Rectangle;
var AdjustmentEvent = java_awt.AdjustmentEvent;
var AdjustmentListener = java_awt.AdjustmentListener;
var MouseEvent = java_awt.MouseEvent;
var MouseListener = java_awt.MouseListener;
var Class = java_lang.Class;
var TreeSet = java_util.TreeSet;
var BorderFactory = javax_swing.BorderFactory;
var SwingUtilities = javax_swing.SwingUtilities;
var ChangeEvent = javax_swing.ChangeEvent;
var ChangeListener = javax_swing.ChangeListener;

/* CommentHighlightMode.js */

var CommentHighlightMode = function() {
   if (!(this instanceof CommentHighlightMode)) return new CommentHighlightMode();
   EditorMode.call(this);
   this.setModeName("CommentHighlightMode");
   this.setStyleColor("comment", CommentHighlightMode.COMMENT_COLOR);
   this.addRule("start", "//.*$", "comment");
   this.addRule("start", "/[*](?:[^*]/|[^/])*[*]/", "comment");
   this.addRule("start", "/[*](?:[^*]/|[^/])*$", "comment", "comment");
   this.addRule("comment", "(?:[^*]/|[^/])*[*]/", "comment", "start");
   this.addRule("comment", "(?:[^*]/|[^/])*$", "comment");
};

CommentHighlightMode.prototype = 
   jslib.inheritPrototype(EditorMode, "CommentHighlightMode extends EditorMode");
CommentHighlightMode.prototype.constructor = CommentHighlightMode;
CommentHighlightMode.prototype.$class = 
   new Class("CommentHighlightMode", CommentHighlightMode);

CommentHighlightMode.COMMENT_COLOR = Color.BLUE;

/* ProgramEditor.js */

var ProgramEditor = function() {
   if (!(this instanceof ProgramEditor)) return new ProgramEditor();
   JSEditor.call(this);
   this.annotationPane = new PEAnnotationPane(this);
   this.add(this.annotationPane, BorderLayout.WEST);
   this.addChangeListener(this.annotationPane);
   this.addAdjustmentListener(this.annotationPane);
   this.breakpoints = new TreeSet();
   this.errorDialog = null;
   this.lastErrorKey = null;
   this.needsParsing = false;
   this.currentLine = 0;
   this.breakpointImage = new JSImage(ProgramEditor.BREAKPOINT_IMAGE);
   this.handImage = new JSImage(ProgramEditor.HAND_IMAGE);
};

ProgramEditor.prototype = 
   jslib.inheritPrototype(JSEditor, "ProgramEditor extends JSEditor");
ProgramEditor.prototype.constructor = ProgramEditor;
ProgramEditor.prototype.$class = 
   new Class("ProgramEditor", ProgramEditor);

ProgramEditor.prototype.setCurrentLine = function(k) {
   this.currentLine = k;
   this.ensureLineVisible(k);
   this.repaint();
};

ProgramEditor.prototype.getCurrentLine = function() {
   return this.currentLine;
};

ProgramEditor.prototype.showErrorDialog = function(msg, k) {
   if (this.errorDialog === null) {
      this.errorDialog = this.createErrorDialog();
   }
   if (this.lastErrorKey !== null) {
      this.removeBackgroundHighlight(this.lastErrorKey);
      this.lastErrorKey = null;
   }
   if (k !== 0) {
      this.lastErrorKey = this.addBackgroundHighlight(k, this.errorDialog.getBackground());
      this.ensureLineVisible(k);
   }
   this.repaint();
   this.errorDialog.setErrorMessage(msg);
   var psize = this.errorDialog.getPreferredSize();
   this.errorDialog.setSize(psize.width, psize.height);
   var pt = new Point((this.getWidth() - this.errorDialog.getWidth()) / 2, (this.getHeight() - this.errorDialog.getHeight()) / 2);
   this.errorDialog.setLocation(this.errorDialog.getWindowCoordinates(pt));
   this.errorDialog.setVisible(true);
};

ProgramEditor.prototype.clearErrorHighlight = function() {
   if (this.lastErrorKey !== null) {
      this.removeBackgroundHighlight(this.lastErrorKey);
   }
};

ProgramEditor.prototype.dismissErrorDialog = function() {
   if (this.errorDialog !== null) this.errorDialog.setVisible(false);
   this.requestFocus();
};

ProgramEditor.prototype.isErrorDialogShowing = function() {
   return this.errorDialog !== null && this.errorDialog.isVisible();
};

ProgramEditor.prototype.updateHighlights = function() {
   var mode = this.getEditorMode();
   if (mode !== null) {
      var needsSaving = this.isSaveNeeded();
      this.setUndoableFlag(false);
      mode.runTokenizer(this);
      this.setSaveNeeded(needsSaving);
      this.setUndoableFlag(true);
   }
};

ProgramEditor.prototype.setBreakpoint = function(k) {
   this.breakpoints.add(this.createMarker(this.getLineStart(k)));
   this.annotationPane.repaint();
};

ProgramEditor.prototype.removeBreakpoint = function(k) {
   this.breakpoints.remove(this.createMarker(this.getLineStart(k)));
   this.annotationPane.repaint();
};

ProgramEditor.prototype.removeAllBreakpoints = function() {
   this.breakpoints.clear();
   this.annotationPane.repaint();
};

ProgramEditor.prototype.isBreakpoint = function(k) {
   return this.breakpoints.contains(this.createMarker(this.getLineStart(k)));
};

ProgramEditor.prototype.isBreakpointLegal = function(k) {
   return true;
};

ProgramEditor.prototype.createErrorDialog = function() {
   return new ProgramErrorDialog(this);
};

ProgramEditor.prototype.drawAnnotations = function(g, k, r) {
   if (this.isBreakpoint(k)) this.drawBreakpoint(g, r);
   if (this.getCurrentLine() === k) this.drawCurrentLineMarker(g, r);
};

ProgramEditor.prototype.setParseNeeded = function(flag) {
   this.needsParsing = flag;
};

ProgramEditor.prototype.isParseNeeded = function() {
   return this.needsParsing;
};

ProgramEditor.prototype.tickle = function() {
   SwingUtilities.invokeLater(new EditorTickler(this));
};

ProgramEditor.prototype.drawCurrentLineMarker = function(g, r) {
   var x = r.x + r.width / 2 + ProgramEditor.HAND_DX;
   var y = r.y + r.height / 2 + ProgramEditor.HAND_DY;
   g.drawImage(this.handImage, x, y, this);
};

ProgramEditor.prototype.drawBreakpoint = function(g, r) {
   var x = r.x + r.width / 2 + ProgramEditor.BREAKPOINT_DX;
   var y = r.y + r.height / 2 + ProgramEditor.BREAKPOINT_DY;
   g.drawImage(this.breakpointImage, x, y, this);
};

ProgramEditor.prototype.getBreakpoints = function() {
   return this.breakpoints;
};

ProgramEditor.BREAKPOINT_IMAGE =
"data:image/png;base64," +
"iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAAPklEQVR42mM4" +
"8/8/A6UYqyBQ+D8uTJQh+AzAZRDJBmAziCwD0A0i2wBkg0YNGfSGUCWdUC3F" +
"Ui3vUC0Xk4MBwEuSveqvlaYAAAAASUVORK5CYII=";
ProgramEditor.HAND_IMAGE =
"data:image/png;base64," +
"iVBORw0KGgoAAAANSUhEUgAAABoAAAAPCAYAAAD6Ud/mAAABPElEQVR42uWU" +
"oZKDQAyGeSLeYZ+AF1iNrsXikLi6U6gqFApThSgGg6mowSAQGATi778X5ijt" +
"wnF3MzXHTAa6k+RL/mTrXADnHeb8T1DoGU/AVTRHvjeNfqsga4A7vQmqWnw9" +
"5w8518l8No7A0APNjb5nQJk4fwa+gph0YKDHb0XHtGCSz0xAoIF6kMRVIv5R" +
"BrQsomkEcq2BIpf4x86soH6UisoRiyfR4pNd5XfkrkjH8yBayrcJKjpWyaTd" +
"ILIk/vpcdi+DtSOCwqeqj4VAa76jw19ASjp4lK6fOjNnXgDEwVxURmDIGEdv" +
"w6xbV3K4vllnJjqmBE8z6jjogxKf3EhKvzTe15UV5E5y6WC+N/EJuJHYlksp" +
"fQ49Ur8EaWofPm2NsixAXtFO053ZK91Pzdwp07nyvl+Et/7X3QHwFTTGgRQj" +
"RQAAAABJRU5ErkJggg==";
ProgramEditor.BREAKPOINT_DX = -9;
ProgramEditor.BREAKPOINT_DY = -11;
ProgramEditor.ERROR_DX = 2;
ProgramEditor.ERROR_DY = 4;
ProgramEditor.HAND_DX = -13;
ProgramEditor.HAND_DY = -6;
var PEAnnotationPane = function(editor) {
   if (!(this instanceof PEAnnotationPane)) return new PEAnnotationPane(editor);
   JSCanvas.call(this);
   this.editor = editor;
   this.setBorder(BorderFactory.createMatteBorder(0, 0, 0, 1, Color.GRAY));
   this.addMouseListener(this);
};

PEAnnotationPane.prototype = 
   jslib.inheritPrototype(JSCanvas, "PEAnnotationPane extends JSCanvas");
PEAnnotationPane.prototype.constructor = PEAnnotationPane;
PEAnnotationPane.prototype.$class = 
   new Class("PEAnnotationPane", PEAnnotationPane);

PEAnnotationPane.prototype.paintComponent = function(g) {
   if (this.needsUpdate) {
      if (this.editor !== null) this.editor.updateHighlights();
      this.needsUpdate = false;
   }
   var size = this.getSize();
   g.setColor(PEAnnotationPane.ANNOTATION_BGCOLOR);
   g.fillRect(0, 0, size.width, size.height);
   var fm = this.editor.getTextPaneMetrics();
   var h = this.editor.getLineHeight();
   var k = this.editor.getTopLine();
   var y0 = this.editor.offsetToPoint(this.editor.getLineStart(k)).y - fm.getAscent();
   var r = new Rectangle(0, y0, size.width, h);
   while (r.y < size.height && this.editor.getLine(k) !== null) {
      this.editor.drawAnnotations(g, k, r);
      r.y += h;
      k++;
   }
};

PEAnnotationPane.prototype.getPreferredSize = function() {
   return new Dimension(PEAnnotationPane.ANNOTATION_WIDTH, 1);
};

PEAnnotationPane.prototype.mouseClicked = function(e) {
   var offset = this.editor.pointToOffset(new Point(0, e.getY()));
   if (offset >= 0) {
      var k = this.editor.getLineNumber(offset);
      if (this.editor.isBreakpoint(k)) {
         this.editor.removeBreakpoint(k);
      } else if (this.editor.isBreakpointLegal(k)) {
         this.editor.setBreakpoint(k);
      }
   }
};

PEAnnotationPane.prototype.mouseEntered = function(e) {
   /* Empty */
};

PEAnnotationPane.prototype.mouseExited = function(e) {
   /* Empty */
};

PEAnnotationPane.prototype.mousePressed = function(e) {
   /* Empty */
};

PEAnnotationPane.prototype.mouseReleased = function(e) {
   /* Empty */
};

PEAnnotationPane.prototype.stateChanged = function(e) {
   if (this.editor.getUndoableFlag()) {
      this.needsUpdate = true;
      this.editor.setParseNeeded(true);
      this.editor.clearErrorHighlight();
      this.repaint();
   }
};

PEAnnotationPane.prototype.adjustmentValueChanged = function(e) {
   this.repaint();
};

PEAnnotationPane.ANNOTATION_BGCOLOR = new Color(0xEEEEEE);
PEAnnotationPane.ANNOTATION_WIDTH = 26;
var EditorTickler = function(editor) {
   if (!(this instanceof EditorTickler)) return new EditorTickler(editor);
   this.editor = editor;
};

EditorTickler.prototype.run = function() {
   try {
      Thread.sleep(2000);
   } catch (ex) {
      /* Empty */
   }
   var n = this.editor.getComponentCount();
   for (var i = 0; i < n; i++) {
      this.editor.getComponent(i).repaint();
   }
   this.editor.repaint();
};


/* ProgramErrorDialog.js */

var ProgramErrorDialog = function(editor) {
   if (!(this instanceof ProgramErrorDialog)) return new ProgramErrorDialog(editor);
   JSErrorDialog.call(this, editor, false);
   this.editor = editor;
};

ProgramErrorDialog.prototype = 
   jslib.inheritPrototype(JSErrorDialog, "ProgramErrorDialog extends JSErrorDialog");
ProgramErrorDialog.prototype.constructor = ProgramErrorDialog;
ProgramErrorDialog.prototype.$class = 
   new Class("ProgramErrorDialog", ProgramErrorDialog);

ProgramErrorDialog.prototype.execute = function(cmd) {
   this.editor.dismissErrorDialog();
};


/* Exports */

return {
   CommentHighlightMode : CommentHighlightMode,
   ProgramEditor : ProgramEditor,
   ProgramErrorDialog : ProgramErrorDialog
};

});
