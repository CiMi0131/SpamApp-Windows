namespace Spam_App
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            label1 = new Label();
            timer1 = new System.Windows.Forms.Timer(components);
            label2 = new Label();
            checkBox1 = new CheckBox();
            textBox1 = new TextBox();
            label3 = new Label();
            textBox2 = new TextBox();
            checkBoxEnter = new CheckBox();
            textBox3 = new TextBox();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Consolas", 20.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label1.ForeColor = Color.FromArgb(230, 230, 230);
            label1.Location = new Point(119, 29);
            label1.Name = "label1";
            label1.Size = new Size(149, 32);
            label1.TabIndex = 1;
            label1.Text = "SPAM MODE";
            // 
            // timer1
            // 
            timer1.Interval = 1;
            timer1.Tick += timer1_Tick;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Consolas", 12.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label2.Location = new Point(250, 93);
            label2.Name = "label2";
            label2.Size = new Size(99, 20);
            label2.TabIndex = 3;
            label2.Text = "Durduruldu";
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Font = new Font("Consolas", 9F, FontStyle.Regular, GraphicsUnit.Point, 0);
            checkBox1.Location = new Point(12, 75);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(187, 46);
            checkBox1.TabIndex = 4;
            checkBox1.Text = "\r\nAçmak için sol tıkla\r\nKapatmak için sağ tıkla\r\n";
            checkBox1.UseVisualStyleBackColor = true;
            checkBox1.CheckedChanged += checkBox1_CheckedChanged;
            checkBox1.MouseDown += checkBox1_MouseDown;
            // 
            // textBox1
            // 
            textBox1.BackColor = Color.FromArgb(75, 75, 75);
            textBox1.BorderStyle = BorderStyle.None;
            textBox1.Font = new Font("Consolas", 9F);
            textBox1.ForeColor = Color.FromArgb(230, 230, 230);
            textBox1.Location = new Point(131, 147);
            textBox1.Multiline = true;
            textBox1.Name = "textBox1";
            textBox1.PlaceholderText = "örnek : a";
            textBox1.Size = new Size(249, 63);
            textBox1.TabIndex = 5;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Consolas", 9F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label3.Location = new Point(12, 149);
            label3.Name = "label3";
            label3.Size = new Size(133, 168);
            label3.TabIndex = 6;
            label3.Text = "YAZILACAK YAZI :\r\n\r\n\r\n\r\n\r\nMS BAŞINA SPAM :\r\n\r\nSPAM LİMİTİ :\r\n\r\nBASILACAK TUŞLAR :\r\n\r\nHOTKEY :    F6";
            
            // 
            // textBox2
            // 
            textBox2.BackColor = Color.FromArgb(75, 75, 75);
            textBox2.BorderStyle = BorderStyle.None;
            textBox2.Font = new Font("Consolas", 9F);
            textBox2.ForeColor = Color.FromArgb(230, 230, 230);
            textBox2.Location = new Point(131, 222);
            textBox2.Name = "textBox2";
            textBox2.PlaceholderText = "1sn 1000ms dir";
            textBox2.Size = new Size(249, 15);
            textBox2.TabIndex = 7;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // checkBoxEnter
            // 
            checkBoxEnter.AutoSize = true;
            checkBoxEnter.Checked = true;
            checkBoxEnter.CheckState = CheckState.Checked;
            checkBoxEnter.Font = new Font("Consolas", 9F, FontStyle.Regular, GraphicsUnit.Point, 0);
            checkBoxEnter.Location = new Point(146, 274);
            checkBoxEnter.Name = "checkBoxEnter";
            checkBoxEnter.Size = new Size(61, 18);
            checkBoxEnter.TabIndex = 9;
            checkBoxEnter.Text = "ENTER";
            checkBoxEnter.UseVisualStyleBackColor = true;
            // 
            // textBox3
            // 
            textBox3.BackColor = Color.FromArgb(75, 75, 75);
            textBox3.BorderStyle = BorderStyle.None;
            textBox3.Font = new Font("Consolas", 9F);
            textBox3.ForeColor = Color.FromArgb(230, 230, 230);
            textBox3.Location = new Point(131, 249);
            textBox3.Name = "textBox3";
            textBox3.PlaceholderText = "örnek: 500 (opsiyonel)";
            textBox3.Size = new Size(249, 15);
            textBox3.TabIndex = 10;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.FromArgb(26, 26, 26);
            ClientSize = new Size(390, 474);
            Controls.Add(textBox3);
            Controls.Add(checkBoxEnter);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(checkBox1);
            Controls.Add(label3);
            ForeColor = Color.FromArgb(230, 230, 230);
            MaximizeBox = false;
            MaximumSize = new Size(406, 513);
            MinimizeBox = false;
            MinimumSize = new Size(406, 513);
            Name = "Form1";
            ShowIcon = false;
            StartPosition = FormStartPosition.CenterScreen;
            Text = "SPAM MODE - Made by CiMi131";
            Load += Form1_Load;
           
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private Label label1;
        private System.Windows.Forms.Timer timer1;
        private Label label2;
        private CheckBox checkBox1;
        private TextBox textBox1;
        private Label label3;
        private TextBox textBox2;
        private CheckBox checkBoxEnter;
        private TextBox textBox3;
    }
}
