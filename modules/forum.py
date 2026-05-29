# modules/forum.py

class ForumModule:
    def __init__(self):
        # Memory-based database tables (Lists of data payloads)
        self.student_Posts = []    # Safe public feed visible to Guests/Visitors
        self.pending_queue = []    # Sandbox holding area for Moderator review
        self.active_Threads = 0    # Track total public posts counter

        # 🛡️ BILINGUAL SECURITY BASELINE
        # Merged the jromest Filipino dataset with the api.dedolist.com English array.
        # Encapsulated with double underscores to ensure strict OOP privacy.
        self.__profanity_blacklist = [
            # --- Filipino Dataset ---
            "amputa", "animal ka", "bilat", "bobo", "boba", "bogok", "boto", 
            "brocha", "burat", "bwuisit", "bwisit", "bwiset", "kantot", "kantutan", 
            "kaulolan", "kayat", "kiki", "puki", "pekpek", "kups", "kupal", 
            "leche", "lintik", "nakakabuwisit", "ogag", "orgasmo", "paq", "pakyaw", 
            "pakyu", "pakshet", "paspas", "piga", "pake", "puke", "puking", 
            "poot", "pucha", "puchangina", "puki", "pukinangina", "puta", 
            "putangina", "putang ina", "putanginammo", "putragis", "puyet", 
            "ratbu", "shabu", "tae", "tanga", "taragis", "tarantado", "tibak", 
            "tite", "titi", "tungunu", "ulol", "hudas", "gago", "gaga",
            
            # --- English Dataset (Sourced & Compiled from api.dedolist.com) ---
            "ass", "asshole", "bastard", "bitch", "bullshit", "cock", "cocksucker",
            "cunt", "dick", "dickhead", "fuck", "fucker", "fucking", "goddamn", 
            "hell", "horseshit", "jackass", "piss", "prick", "pussy", "shit", 
            "shite", "slut", "twat", "wanker", "whore"
        ]

    def check_for_spam(self, text_input: str) -> bool:
        """
        Automated Security Filter: Normalizes text and evaluates content against the blacklist.
        Returns True if profane terms are matched, otherwise False.
        """
        # Lowercase incoming strings so users can't bypass via capitalization (e.g., "BoBo", "FucK")
        cleaned_input = text_input.lower()
        
        for bad_word in self.__profanity_blacklist:
            if bad_word in cleaned_input:
                return True
        return False

    def create_Post(self, author: str, title: str, content: str) -> tuple[bool, str]: 
        """
        Processes a submission attempt. Intercepts inappropriate language via automated filters.
        If clean, logs it straight into the pending queue for staff confirmation.
        """
        # Run automated safety gate check
        if self.check_for_spam(title) or self.check_for_spam(content):
            return False, "Submission Blocked: Inappropriate or profane language detected."

        # Sandbox the post payload
        post_payload = {
            "post_id": len(self.student_Posts) + len(self.pending_queue) + 1,
            "author": author,
            "title": title,
            "content": content,
            "status": "pending"
        }
        self.pending_queue.append(post_payload)
        return True, "Post submitted successfully! Awaiting moderator validation."

    def view_threads(self) -> list: 
        """
        Returns only approved, public posts. Safely served to Guest/Visitor view states.
        """
        return self.student_Posts

    # --- STAFF ADMINISTRATION METHODS ---

    def get_pending_queue(self) -> list:
        """Allows Admins/Moderators to check sandbox queues."""
        return self.pending_queue

    def approve_post(self, post_id: int) -> bool:
        """Moves a post from the pending queue into the active public threads list."""
        for post in self.pending_queue:
            if post["post_id"] == post_id:
                post["status"] = "approved"
                self.student_Posts.append(post)
                self.pending_queue.remove(post)
                self.active_Threads = len(self.student_Posts)
                return True
        return False

    def reject_post(self, post_id: int) -> bool:
        """Deletes a toxic or invalid submission entirely out of the system queues."""
        for post in self.pending_queue:
            if post["post_id"] == post_id:
                self.pending_queue.remove(post)
                return True
        return False

    def report_Post(self, postID: int): 
        """Allows users to flag active public posts."""
        for post in self.student_Posts:
            if post["post_id"] == postID:
                post["status"] = "reported"
                # Push it back to the pending queue for re-evaluation
                self.pending_queue.append(post)
                self.student_Posts.remove(post)
                self.active_Threads = len(self.student_Posts)
                return True
        return False