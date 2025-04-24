<script setup lang="ts">

</script>

<template>
  <PageContainer>
    <h1>Projects</h1>
    <h2>Active Projects</h2>
    <p>These are the projects we're currently working on.</p>
    <div class="projects">
      <ProjectCard
          title="DevU"
          description="An automatic code grading platform for programming assignments with a full-featured API"
          link="/projects/devu"
      />
      <ProjectCard
          title="mOS"
          description="A simple operating system created from scratch"
          link="/projects/operating-system"
          image-url="/logo.png"
      />
      <ProjectCard
          title="Buffalo Transit"
          description="Todo"
          link="/projects/buffalo-transit"
      />
      <ProjectCard
          title="Make Office Hours"
          description="Todo"
          link="/projects/office-hours"
      />
      <ProjectCard
          title="Flappy Bird VR"
          description="Todo"
          link="/projects/flappy-bird-vr"
      />


    </div>

    <h2>Previous Projects</h2>
    <p>These are projects we've worked on in the past.</p>
    <div class="projects">
      <ProjectCard
          title="Modules"
          description="Todo"
      />
      <ProjectCard
          title="Dotdot"
          description="Todo"
      />
      <ProjectCard
          title="Classic RPG"
          description="Todo"
      />
      <ProjectCard
          title="Authenticator"
          description="Todo"
      />
    </div>
  </PageContainer>
</template>

<style scoped>
.projects {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  margin-bottom: 48px;
}

</style>