using System;
using System.Runtime.InteropServices;
using System.Text;
using System.Windows.Forms;

namespace Spam_App
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", SetLastError = true)]
        private static extern bool RegisterHotKey(IntPtr hWnd, int id, int fsModifiers, int vk);

        [DllImport("user32.dll", SetLastError = true)]
        private static extern bool UnregisterHotKey(IntPtr hWnd, int id);

        private const int HOTKEY_ID = 1;
        private const int WM_HOTKEY = 0x0312;

        // Durum Değişkenleri
        private int geriSayim = 3;
        private int spamSayaci = 0;
        private int spamLimiti = 0;
        private bool isHotKeyRegistered = false;

        // Timer nesnesi
        private System.Windows.Forms.Timer geriSayimTimer;

        public Form1()
        {
            InitializeComponent();
            geriSayimTimer = new System.Windows.Forms.Timer();
        }

        protected override void WndProc(ref Message m)
        {
            if (m.Msg == WM_HOTKEY && m.WParam.ToInt32() == HOTKEY_ID)
            {
                checkBox1.Checked = !checkBox1.Checked;
            }
            base.WndProc(ref m);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            geriSayimTimer.Interval = 1000;
            geriSayimTimer.Tick += GeriSayimTimer_Tick;
            isHotKeyRegistered = RegisterHotKey(this.Handle, HOTKEY_ID, 0, (int)Keys.F6);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string text = textBox1.Text;

            if (!string.IsNullOrEmpty(text))
            {
                try
                {
                    string safeText = EncodeSendKeysText(text);
                    SendKeys.Send(safeText);
                }
                catch
                {

                }
            }
            if (checkBoxEnter.Checked)
            {
                SendKeys.Send("{ENTER}");
            }

            // Limit Kontrolü
            if (spamLimiti > 0)
            {
                spamSayaci++;
                if (spamSayaci >= spamLimiti)
                {
                    StopSpam("Limit doldu.");
                }
            }
        }
        private string EncodeSendKeysText(string input)
        {
            if (string.IsNullOrEmpty(input)) return input;

            StringBuilder sb = new StringBuilder();
            foreach (char c in input)
            {
                if (c == '+' || c == '^' || c == '%' || c == '~' ||
                    c == '(' || c == ')' || c == '{' || c == '}' ||
                    c == '[' || c == ']')
                {
                    sb.Append($"{{{c}}}");
                }
                else
                {
                    sb.Append(c);
                }
            }
            return sb.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            checkBox1.Checked = true;
        }

        private void GeriSayimTimer_Tick(object sender, EventArgs e)
        {
            if (geriSayim > 0)
            {
                label2.Text = $"{geriSayim}...";
                geriSayim--;
            }
            else
            {
                geriSayimTimer.Stop();
                geriSayim = 3;
                spamSayaci = 0;

                timer1.Start();
                label2.Text = "ÇALIŞIYOR!";
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                if (string.IsNullOrWhiteSpace(textBox2.Text) || string.IsNullOrWhiteSpace(textBox1.Text))
                {
                    checkBox1.Checked = false;
                    MessageBox.Show("Değer boş olamaz", "Spam App", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                if (!int.TryParse(textBox3.Text, out spamLimiti) || spamLimiti < 0)
                {
                    spamLimiti = 0;
                }

                ToggleUI(false);
                geriSayim = 3;
                label2.Text = "3...";
                geriSayimTimer.Start();
            }
            else
            {
                StopSpam("Durduruldu.");
            }
        }

        private void StopSpam(string message)
        {
            geriSayimTimer.Stop();
            timer1.Stop();
            geriSayim = 3;
            spamSayaci = 0;

            label2.Text = message;
            checkBox1.Checked = false;
            ToggleUI(true);
        }

        private void ToggleUI(bool enable)
        {
            textBox1.Enabled = enable;
            textBox2.Enabled = enable;
            textBox3.Enabled = enable;
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            if (int.TryParse(textBox2.Text, out int interval) && interval > 0)
            {
                timer1.Interval = interval;
            }
        }

        private void checkBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                checkBox1.Checked = false;
            }
        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            if (isHotKeyRegistered)
            {
                UnregisterHotKey(this.Handle, HOTKEY_ID);
            }
            base.OnFormClosing(e);
        }
    }
}
